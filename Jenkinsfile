pipeline {
    agent any

    environment {
        PATH_TO_HOST_FOLDER = pwd()
        SEMGREP_APP_TOKEN = credentials('SEMGREP_APP_TOKEN')
    }

    stages {
        // ... (existing stages)

        // stage('GitLeaks Scan') {
        //     steps {
        //         catchError(buildResult: 'SUCCESS') {
        //             script {
        //                 sh 'docker pull zricethezav/gitleaks:latest'
        //                 sh "docker run --rm -v /var/lib/jenkins/workspace/juice-shop:/path zricethezav/gitleaks:latest detect --source=/path --report-format json --report-path /path/gitleaks_scan.json"
        //                 // archiveArtifacts artifacts: 'gitleaks_scan.json', fingerprint: true
        //             }
        //         }
        //     }
        // }

        // stage('njs Scan') {
        //     steps {
        //         catchError(buildResult: 'SUCCESS') {
        //             script {
        //                 sh "docker pull opensecurity/njsscan"
        //                 sh "docker run --rm -v \"${PATH_TO_HOST_FOLDER}\":/path opensecurity/njsscan /path --exit-warning --sarif --output /path/njs_scan.sarif"
        //                 // archiveArtifacts artifacts: 'njs_scan.sarif', fingerprint: true
        //             }
        //         }
        //     }
        // }

        // stage('semgrep Scan') {
        //     steps {
        //         catchError(buildResult: 'SUCCESS') {
        //             script {
        //                 sh 'docker pull returntocorp/semgrep'
        //                 sh "docker run -e SEMGREP_APP_TOKEN=${SEMGREP_APP_TOKEN} --rm -v \"${PATH_TO_HOST_FOLDER}\":/src returntocorp/semgrep semgrep --config \"p/javascript\" --json --output semgrep_scan.json"
        //                 // archiveArtifacts artifacts: 'semgrep_scan.json', fingerprint: true
        //             }
        //         }
        //     }
        // }
        stage('JS vulnerability check') {
            steps {
                catchError(buildResult: 'SUCCESS') {
                    script {
                        sh "docker build -t retirescan ./Dockerfileretirescan"
                        sh "docker run --rm -v \"${PATH_TO_HOST_FOLDER}\":/app retirescan"
                        // archiveArtifacts artifacts: 'gitleaks_scan.json', fingerprint: true
                    }
                }
            }
        }               
        stage('Upload Reports'){
            steps {
                script {
                    sh "docker build -t uploadreport ./Dockerfile-scan-reports"
                    // sh "docker run --rm -v \"${PATH_TO_HOST_FOLDER}\":/app uploadreport python upload-reports.py gitleaks_scan.json"
                    // sh "docker run --rm -v \"${PATH_TO_HOST_FOLDER}\":/app uploadreport python upload-reports.py njs_scan.sarif"
                    // sh "docker run --rm -v \"${PATH_TO_HOST_FOLDER}\":/app uploadreport python upload-reports.py semgrep_scan.json"
                    sh "docker run --rm -v \"${PATH_TO_HOST_FOLDER}\":/app uploadreport python upload-reports.py retirejs_scan.json"
                }
            }
        }
    }
    post {
        always {
            // archiveArtifacts 'gitleaks_scan.json'
            // archiveArtifacts 'njs_scan.sarif'
            // archiveArtifacts 'semgrep_scan.json'
            archiveArtifacts 'retirejs_scan.json'
        }
    }    

}
