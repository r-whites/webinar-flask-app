podTemplate(label: 'docker', containers: [containerTemplate(image: 'docker', name: 'docker', command: 'cat', ttyEnabled: true)]) {
    podTemplate(label: 'pytest', containers: [containerTemplate(image: 'qnib/pytest', name: 'maven', command: 'cat', ttyEnabled: true)]) {
        pipeline {
            stages {
                stage('Test') {
                    steps {
                        echo 'Testing..'
                    }
                }
                stage('Build') {
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
    }
}
