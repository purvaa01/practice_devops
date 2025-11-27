pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests With Coverage') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --cov=. --cov-report=xml --cov-report=term
                '''
            }
        }
    }

    post {
        success { echo 'build succeeded!' }
        failure { echo 'build failed!' }
    }
}
