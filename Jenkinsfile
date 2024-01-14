pipeline {
    agent any

    environment {
        PATH_TO_HOST_FOLDER = pwd()
    }

    stages {
        stage('GitHub Connection') {
            steps {
                catchError(buildResult: 'SUCCESS') {
                    checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/EAwangya/juice-shop.git']]])
                }
            }
        }

        stage('GitLeaks Scanner') {
            steps {
                catchError(buildResult: 'SUCCESS') {
                    script {
                        // Uncomment the following line if you haven't pulled the Docker image yet
                        // sh 'docker pull zricethezav/gitleaks:latest'

                        sh "docker run -v \"${PATH_TO_HOST_FOLDER}\":/path zricethezav/gitleaks:latest detect --source=/path"
                    }
                }
            }
        }
    }
}
