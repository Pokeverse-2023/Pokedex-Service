provider "aws" {
  region = var.region

  default_tags {
    tags = var.default_tags
  }
}

module "Pokedex-Service" {
  source        = "./modules/services"
  function_name = var.function_name
  handler_name  = var.handler
  runtime       = var.function_runtime
  memory_size   = var.memory
  timeout_limit = var.timeout
  source_code   = var.source_code_path
  output_path   = var.output_path
}
