variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "environment" {
  description = "Environment name (e.g., dev, staging, prod)"
  type        = string
}

variable "project_name" {
  description = "Name of the project"
  type        = string
}

resource "google_compute_instance_template" "main" {
  name_prefix  = "${var.project_name}-${var.environment}-template"
  machine_type = "e2-micro"
  region       = var.region

  disk {
    source_image = "debian-cloud/debian-10"
    auto_delete  = true
    boot         = true
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = templatefile("${path.module}/templates/startup.sh", {
    project_name = var.project_name
    environment  = var.environment
  })

  tags = ["${var.project_name}-${var.environment}"]

  labels = {
    environment = var.environment
    project     = var.project_name
    terraform   = "true"
  }
}

resource "google_compute_instance_group_manager" "main" {
  name = "${var.project_name}-${var.environment}-igm"

  base_instance_name = "${var.project_name}-${var.environment}"
  zone              = "${var.region}-a"

  version {
    instance_template = google_compute_instance_template.main.id
  }

  target_size = 1

  named_port {
    name = "http"
    port = 80
  }
} 