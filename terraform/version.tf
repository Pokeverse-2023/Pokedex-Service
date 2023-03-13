terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.58.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.2.1"
    }
    http = {
      source  = "hashicorp/http"
      version = "~> 3.2.1"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.4.3"
    }
  }

  required_version = "~> 1.3.9"
}