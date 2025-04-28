pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/ARYANSINGH0611/DevOps.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --html=reports/report.html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/report.html', fingerprint: true
        }
        success {
            emailext (
                subject: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build completed successfully. Find the report attached.",
                to: "your-email@example.com",
                attachmentsPattern: "reports/report.html"
            )
        }
        failure {
            emailext (
                subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build failed. Please check Jenkins logs for details.",
                to: "aryansingharyan322@gmail.com"
            )
        }
    }
}
