output "connection_url"{
    value = mongodbatlas_cluster.mongodb_cluster.connection_strings[0].standard_srv
}

output "mongodb_username"{
    value = mongodbatlas_database_user.mongodb_user.username
}

output "mongodb_password"{
    value = mongodbatlas_database_user.mongodb_user.password
}
