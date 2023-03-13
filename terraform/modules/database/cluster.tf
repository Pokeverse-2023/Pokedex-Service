resource "mongodbatlas_cluster" "mongodb_cluster" {
  project_id                  = mongodbatlas_project.mongodb_project.id
  name                        = var.cluster_name
  provider_instance_size_name = "M0"
  provider_name               = "TENANT"
  backing_provider_name       = "AWS"
  provider_region_name        = "AP_SOUTH_1"
}
