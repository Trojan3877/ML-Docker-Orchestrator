# terraform/main.tf

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "ml_api_server" {
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux 2 (check for latest)
  instance_type = "t2.micro"

  tags = {
    Name = "ML-Docker-Orchestrator-Server"
  }

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              amazon-linux-extras install docker -y
              service docker start
              usermod -a -G docker ec2-user
              docker run -d -p 8000:8000 ml-docker-api
              EOF
}
