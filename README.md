# 🚀 ML-Docker-Orchestrator with Full MLops Pipeline

A containerized machine learning deployment pipeline using **PyTorch**, **Docker Compose**, **Kubernetes**, **Terraform**, **Ansible**, **Apache Kafka**, and **Snowflake**.
https://codecov.io/gh/Trojan3877/ML-Docker-Orchestrator/branch/main/graph/badge.svg
![Coverage](https://codecov.io/gh/Trojan3877/<REPO>/branch/main/graph/badge.svg)


![Docker](https://img.shields.io/badge/Containerized-Docker-informational)
![Kubernetes](https://img.shields.io/badge/Orchestrator-Kubernetes-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-success)
![ML-Framework](https://img.shields.io/badge/Framework-PyTorch-red)
![IaC](https://img.shields.io/badge/Infrastructure-Terraform-purple)
![Provisioning](https://img.shields.io/badge/Provisioning-Ansible-yellow)
![Streaming](https://img.shields.io/badge/Streaming-Apache_Kafka-orange)
![DataWarehouse](https://img.shields.io/badge/Data-Snowflake-lightblue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🧠 Architecture Flowchart

![image](https://github.com/user-attachments/assets/d9044d80-a9d7-42f7-8957-19bd2e9e9e77)



---

## 📂 Project Structure

```plaintext
ML-Docker-Orchestrator/
├── model/train.py
├── app/main.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── k8s/deployment.yaml
├── terraform/main.tf
├── ansible/provision.yml
├── snowflake/connect_snowflake.py
├── apache/stream_data.py
├── tests/test_api.py
├── notebooks/eda_snowflake_data.ipynb
├── .github/workflows/ci.yml
├── Makefile
├── requirements.txt
├── .env.example
├── CONTRIBUTING.md
├── CHANGELOG.md
├── README.md
└── visual_flowchart.png
