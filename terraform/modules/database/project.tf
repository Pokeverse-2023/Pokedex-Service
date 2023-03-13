resource "mongodbatlas_project" "mongodb_project" {
  name   = var.project_name
  org_id = data.mongodbatlas_roles_org_id.mongodb_org.id
}
