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
                    echo 'pytest'
                }
            }
        }
        stage('Build') {
            steps {
                container('docker') {
                    echo 'docker build -t flask-app .'
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
