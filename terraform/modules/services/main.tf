resource "aws_lambda_function" "lambda-service" {
  function_name = var.function_name
  description   = var.description
  handler       = var.handler_name
  runtime       = var.runtime

  role        = aws_iam_role.lambda_exec_role.arn
  memory_size = var.memory_size
  timeout     = var.timeout_limit

  depends_on       = [null_resource.install_python_dependencies]
  source_code_hash = data.archive_file.create_dist_pkg.output_base64sha256
  filename         = data.archive_file.create_dist_pkg.output_path
}
