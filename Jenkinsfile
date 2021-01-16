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
                        sh 'pip install -r requirements.txt'
                        sh 'pytest'
                    }
                }
            }
        }
        stage('Build') {
            steps {
                container('docker-client') {
                    sh 'docker build . -t localhost:32000/webinar:flask-app'
                    ah 'docker push localhost:32000/webinar'
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
