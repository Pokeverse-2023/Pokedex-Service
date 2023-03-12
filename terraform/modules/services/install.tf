resource "null_resource" "install_python_dependencies" {
  provisioner "local-exec" {
    command = "bash ${path.module}/scripts/build_pkg.sh"

    environment = {
      source_code_path = var.source_code
      function_name = var.function_name
      path_module = path.module
      runtime = var.runtime
      path_cwd = path.cwd
    }
  }
}