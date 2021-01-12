pipeline {
    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'build.yaml'
        }
    }
    stages {
        stage('Test') {
            steps {
                container('pytest') {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest'
                }
            }
        }
        stage('Build') {
            steps {
                container('docker') {
                    sh 'docker build -t flask-app .'
                }
            }
        }
        stage('Deploy') {
            steps {
                container('docker') {
                    sh 'kubectl get pods -n jenkins'
                }
            }
        }
    }
}
