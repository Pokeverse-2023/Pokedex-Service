terraform {
  backend "s3" {
    bucket = "pokeverse"
    key    = "terraform/all-state/terraform.tfstate"
    region = "ap-south-1"
  }
}

module "Pokedex-Service" {
  source               = "git::https://github.com/pokeverse-2023/terraform-hub.git//services"
  function_name        = var.function_name
  function_runtime     = var.function_runtime
  handler              = var.handler
  memory               = var.memory
  default_tags         = var.default_tags
  mongodb_cluster_name = var.mongodb_cluster_name
  mongodb_private_key  = var.mongodb_private_key
  mongodb_project_name = var.mongodb_project_name
  mongodb_public_key   = var.mongodb_public_key
  mongodb_username     = var.mongodb_username
  source_code_path     = var.source_code_path
  timeout              = var.timeout
  output_path          = var.output_path
  region               = var.region
}
