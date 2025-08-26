# Makefile for AI & ML Training Project
.PHONY: help install install-dev setup clean test lint format check-format run-notebooks deploy-streamlit deploy-fastapi

# Default target
help:
	@echo "Available commands:"
	@echo "  install      - Install core dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo "  setup        - Setup development environment"
	@echo "  clean        - Clean cache and build files"
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting (flake8)"
	@echo "  format       - Format code (black + isort)"
	@echo "  check-format - Check code formatting"
	@echo "  run-notebooks - Start Jupyter Lab"
	@echo "  deploy-streamlit - Run Streamlit app"
	@echo "  deploy-fastapi - Run FastAPI app"

# Installation
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -e ".[dev]"

setup: install-dev
	pre-commit install
	@echo "Development environment setup complete!"

# Cleaning
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	rm -rf build/ dist/

# Testing
test:
	pytest tests/ -v

test-coverage:
	pytest tests/ --cov=src --cov-report=html --cov-report=term

# Code Quality
lint:
	flake8 src/ tests/ scripts/

format:
	black src/ tests/ scripts/
	isort src/ tests/ scripts/

check-format:
	black --check src/ tests/ scripts/
	isort --check-only src/ tests/ scripts/

# Development
run-notebooks:
	jupyter lab

run-notebook-server:
	jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser

# Deployment
deploy-streamlit:
	streamlit run deployments/streamlit/app.py

deploy-fastapi:
	uvicorn deployments.fastapi.main:app --host 0.0.0.0 --port 8000 --reload

# Data
download-data:
	python scripts/download_data.py

# Training
train-model:
	python scripts/train_model.py

evaluate-model:
	python scripts/evaluate_model.py

# Docker (if needed)
docker-build:
	docker build -t ai-ml-training .

docker-run:
	docker run -p 8888:8888 ai-ml-training

# Git hooks
pre-commit-all:
	pre-commit run --all-files
