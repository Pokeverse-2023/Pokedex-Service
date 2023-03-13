terraform {
  backend "s3" {
    bucket = "pokeverse"
    key    = "terraform/all-state/terraform.tfstate"
    region = "ap-south-1"
  }
}
