pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests With Coverage') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --cov=src --cov-report=xml --cov-report=term
                '''
            }
        }

    }
    post {
        success { echo 'build succeded!' }
        failure { echo 'build failed!'}
    }
}