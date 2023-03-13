resource "random_password" "mongodb_password" {
  length           = 12
  special          = true
  override_special = "!&"
}

resource "mongodbatlas_database_user" "mongodb_user" {
  username            = var.username
  password            = random_password.mongodb_password.result
  project_id          = mongodbatlas_project.mongodb_project.id
  auth_database_name = "admin"

  roles {
    role_name     = "readWrite"
    database_name = "Pokedex"
  }

  scopes {
    name = mongodbatlas_cluster.mongodb_cluster.name
    type = "CLUSTER"
  }
}
