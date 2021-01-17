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
                    dir('app') {
                        sh "echo 'Testing ..'"
                        // sh 'pip install -r requirements.txt'
                        // sh 'pytest'
                    }
                }
            }
        }
        stage('Build') {
            steps {
                container('docker-client') {
                    sh 'docker build . -t webinar:flask-app'
                    sh 'docker save webinar > webinar.tar'
                    sh 'microk8s ctr image import webinar.tar'
                }
            }
        }
        stage('Deploy') {
            steps {
                container('kubectl') {
                    sh 'kubectl apply -f deployment.yaml'
                }
            }
        }
    }
}
