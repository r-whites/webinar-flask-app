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
                    echo 'Testing ..'
                }
            }
        }
        stage('Build') {
            steps {
                container('docker') {
                    echo 'Building ..'
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
