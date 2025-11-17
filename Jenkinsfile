pipeline {
    agent any

    environment {
        DOCKER_CREDS = credentials('docker-hub')
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Meghana2417/AuthService.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build --no-cache -t meghana1724/authservice:latest ."
            }
        }

        stage('Docker Login') {
            steps {
                sh 'echo "$DOCKER_CREDS_PSW" | docker login -u "$DOCKER_CREDS_USR" --password-stdin'
            }
        }

        stage('Docker Push') {
            steps {
                sh "docker push meghana1724/authservice:latest"
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop authservice || true
                docker rm authservice || true

                docker pull meghana1724/authservice:latest

                docker run -d --name authservice -p 8001:8001 meghana1724/authservice:latest
                '''
            }
        }
    }
}
