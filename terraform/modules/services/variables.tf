variable "function_name" {
  type = string
}

variable "description" {
  type    = string
  default = "A Service For The Pokedex Module"
}

variable "handler_name" {
  type = string
}

variable "runtime" {
  type = string
}

variable "memory_size"{
  type = string
}

variable "timeout_limit"{
  type = string
}

variable "source_code"{
  type = string
}

variable "output_path"{
  type = string
}
