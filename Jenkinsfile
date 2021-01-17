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
                    sh 'docker build . -t 193.204.79.237:3200/webinar:flask-app'
                    sh 'docker push 193.204.79.237:3200/webinar'
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
