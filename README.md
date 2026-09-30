# Docker CI/CD Pipeline

A DevOps practice project demonstrating containerization and a basic CI/CD workflow.

## Architecture
Developer -> Git -> Jenkins -> Docker Build -> Container -> Health Check

## Technologies
Python, Flask, Docker, Jenkins, Git, Linux

## Run Locally
```bash
docker build -t devops-demo .
docker run -p 5000:5000 devops-demo
```

Open `http://localhost:5000` and `http://localhost:5000/health`.

## Note
The Jenkinsfile is a starter pipeline for a Linux Jenkins agent with Docker available.
