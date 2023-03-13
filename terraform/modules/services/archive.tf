data "archive_file" "create_dist_pkg" {
  depends_on = [null_resource.install_python_dependencies]
  source_dir = "${path.cwd}/build_pkg/"
  output_path = var.output_path
  type = "zip"
}
