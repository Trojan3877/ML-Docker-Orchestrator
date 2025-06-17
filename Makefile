
# Makefile for ML-Docker-Orchestrator

# Build Docker image
build:
	docker build -t ml-docker-api -f docker/Dockerfile .

# Run Docker container
run:
	docker run -d -p 8000:8000 --name ml_docker_app ml-docker-api

# Stop and remove container
stop:
	docker stop ml_docker_app || true
	docker rm ml_docker_app || true

# Clean up image
clean:
	docker rmi ml-docker-api || true

# Run all tests
test:
	pytest tests/

# Lint code with flake8
lint:
	flake8 app/ model/

# Run API locally
serve:
	uvicorn app.main:app --reload

# Build and start with Docker Compose
compose-up:
	docker-compose -f docker/docker-compose.yml up --build

# Tear down Docker Compose
compose-down:
	docker-compose -f docker/docker-compose.yml down
