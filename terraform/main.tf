provider "aws" {
  region = var.region

  default_tags {
    tags = var.default_tags
  }
}

module "Mongo-DB" {
  source          = "./modules/database"
  public_key      = var.mongodb_public_key
  private_key     = var.mongodb_private_key
  cluster_name    = var.mongodb_cluster_name
  project_name    = var.mongodb_project_name
  username        = var.mongodb_username
}

module "Pokedex-Service" {
  depends_on = [
    module.Mongo-DB
  ]
  source        = "./modules/services"
  function_name = var.function_name
  handler_name  = var.handler
  runtime       = var.function_runtime
  env_conf = {
    DB_NAME     = "Pokedex"
    DB_PASSWORD = module.Mongo-DB.mongodb_password
    DB_SETTINGS = "?retryWrites=true&w=majority"
    DB_URL      = replace(module.Mongo-DB.connection_url, "mongodb+srv://", "mongodb+srv://${module.Mongo-DB.mongodb_username}:${coalesce(nonsensitive(module.Mongo-DB.mongodb_password), "null")}@")
    DB_USER     = module.Mongo-DB.mongodb_username
  }
  memory_size   = var.memory
  timeout_limit = var.timeout
  source_code   = var.source_code_path
  output_path   = var.output_path
}

resource "null_resource" "clean-up" {
  triggers = {
    always_run = "${timestamp()}"
  }
  depends_on = [
    module.Pokedex-Service
  ]
  provisioner "local-exec" {
    command = join(" && ", [
      "rm -f -R build*",
      "rm -f -R *-repo",
    ])
  }
}
