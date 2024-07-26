terraform {
  #minimum terraform version to run
  required_version = ">= 1.5.5"

  #library/modules need to be call
  required_providers {

    azuredevops = {
      source  = "microsoft/azuredevops"
      version = ">=1.1.1"
    }
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
    cloudflare = {
      source = "cloudflare/cloudflare"
      version = "~> 4.0"
    }
  }
}


provider "digitalocean" {
  token = var.TOKEN_DIGITAL_OCEAN
}
provider "azuredevops" {
  org_service_url = "https://dev.azure.com/digicorpslab/"
  personal_access_token = var.AZURE_DEVOPS_PAT_TOKEN
}
provider "cloudflare" {
  api_token = var.CLOUDFLARE_API_TOKEN
}

#ssh
data "digitalocean_ssh_key" "cocoy" {
  name = "Cocoy"
}

# Create VPS
resource "digitalocean_droplet" "pocio" {
  image  = "docker-20-04"
  name   = "dgmv-poc-${var.ENVIRONMENT_INSTANCE}"
  region = "fra1"
  size   = "s-1vcpu-2gb"
  # Optional SSH Key Configuration
  ssh_keys = [
    data.digitalocean_ssh_key.cocoy.id
  ]

  tags = ["automated", "${var.ENVIRONMENT_INSTANCE}"]
}


data "azuredevops_project" "dgmv_azdo_project" {
  name = "Public"
}

resource "azuredevops_serviceendpoint_ssh" "azdo_ssh" {
  project_id            = data.azuredevops_project.dgmv_azdo_project.id
  service_endpoint_name = "automate-poc-${var.ENVIRONMENT_INSTANCE}"
  host                  = digitalocean_droplet.pocio.ipv4_address
  username              = "root"
  description           = "Managed by Terraform ${var.ENVIRONMENT_INSTANCE} poc"
}

data "cloudflare_zone" "dgmv_domain" {
  name = "digithreelabs.com"
}

resource "cloudflare_record" "weblicense" {
  zone_id = data.cloudflare_zone.dgmv_domain.zone_id
  name    = "cocoytest"
  value   = digitalocean_droplet.pocio.ipv4_address
  type    = "A"
  proxied = true
  comment = "Automate Manage Via DevOps ${var.ENVIRONMENT_INSTANCE} "
}


output "droplet_ip_license" {
  value = digitalocean_droplet.pocio.ipv4_address
}
