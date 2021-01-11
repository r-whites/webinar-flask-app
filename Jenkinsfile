pipeline {
    stages {
        stage('Test') {
            agent {
                label 'pytest'
            }
            steps {
                echo 'Testing..'
            }
        }
        stage('Build') {
            agent {
                docker { image 'docker'}
            }
            steps {
                echo 'Building..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
