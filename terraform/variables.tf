variable "region" {
  type    = string
  default = "ap-south-1"
}

variable "default_tags" {
  type = object({
    Terraform    = bool
    Service      = string
    Organization = string
  })
}

variable "function_name" {
  type = string
}

variable "function_runtime" {
  type = string
}

variable "handler" {
  type = string
}

variable "memory" {
  type = number
}

variable "timeout" {
  type = number
}

variable "source_code_path" {
  type = string
}

variable "output_path"{
  type = string
}