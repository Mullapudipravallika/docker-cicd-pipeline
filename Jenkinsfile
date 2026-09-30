pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source checkout stage'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-demo .'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Run application health checks'
            }
        }
    }
}
