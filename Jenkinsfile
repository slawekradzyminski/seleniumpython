pipeline {
    agent any
    stages {
        stage('Dependencies install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run test') {
            steps {
                sh 'pytest tests/test_math.py'
            }
        }
    }
}