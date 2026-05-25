pipeline{
    agent any

    stages{
        stage('Clone Reporsitory'){
            steps{
                git 'https://github.com/yourusername/banking-transaction-monitor.git'
            }
        }

        stage('Build Docker Image'){
            steps{
                sh 'docker build -t banking-monitor .'
            }
        }

        stage('Run Container'){
            steps{
                sh 'docker run -d -p 5000:5000 banking-monitor'
            }
        }

        stage('Health Check'){
            steps{
                sh 'bash scripts/health-check.sh'
            }
        }
    }
}