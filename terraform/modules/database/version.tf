terraform {
  required_providers {
    mongodbatlas = {
      source = "mongodb/mongodbatlas"
      version = "1.8.1"
    }
  }

  required_version = "~> 1.3.9"
}
