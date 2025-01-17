terraform {
  required_version = ">= 1.0.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
}

variable "cloud_provider" {
  description = "Which cloud provider to use (aws, azure, or gcp)"
  type        = string
}

variable "project_name" {
  description = "Name of the project"
  type        = string
}

variable "environment" {
  description = "Environment name (e.g., dev, staging, prod)"
  type        = string
}

module "aws_infrastructure" {
  count  = var.cloud_provider == "aws" ? 1 : 0
  source = "../modules/aws_ec2_asg"

  project_name = var.project_name
  environment  = var.environment
}

module "azure_infrastructure" {
  count  = var.cloud_provider == "azure" ? 1 : 0
  source = "../modules/azure_vm_scale_set"

  project_name         = var.project_name
  environment         = var.environment
  resource_group_name = "my-resource-group"
  location           = "eastus"
}

module "gcp_infrastructure" {
  count  = var.cloud_provider == "gcp" ? 1 : 0
  source = "../modules/gcp_instance_group"

  project_name = var.project_name
  environment  = var.environment
  project_id  = "my-project-id"
  region      = "us-central1"
} 