variable "ENVIRONMENT_INSTANCE" {
    type = string
    description = <<EOT
    (Required) Environment Instance of the Resource

    Default: production
    EOT
    default = "production"
    sensitive = false
}

variable "TOKEN_DIGITAL_OCEAN" {
    type = string
    description = <<EOT
    (Required) Digital Ocean API Token.
    EOT
    sensitive = true
}

variable "AZURE_DEVOPS_PAT_TOKEN" {
    type = string
    description = <<EOT
    (Required) Azure DevOps PAT Token.
    EOT
    sensitive = true
}

variable "CLOUDFLARE_API_TOKEN" {
    type = string
    description = <<EOT
    (Required) Cloud Flare API Key.
    EOT
    sensitive = true
}
