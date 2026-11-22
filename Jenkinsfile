pipeline {
    agent any

    environment {
        VENV_DIR   = 'venv'
        DEPLOY_DIR = 'C:\\JenkinsDeploy\\PyJen001'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 15, unit: 'MINUTES')
    }

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python --version'
                bat 'python -m venv %VENV_DIR%'
                bat '%VENV_DIR%\\Scripts\\python -m pip install --upgrade pip'
                bat '%VENV_DIR%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                bat '%VENV_DIR%\\Scripts\\flake8 --max-line-length=100 --exclude=%VENV_DIR% .'
            }
        }

        stage('Test') {
            steps {
                bat '%VENV_DIR%\\Scripts\\pytest -v --junitxml=reports\\results.xml'
            }
        }

        stage('Build') {
            steps {
                bat 'if not exist dist mkdir dist'
                bat 'powershell -NoProfile -Command "Compress-Archive -Path *.py -DestinationPath dist\\PyJen001-%BUILD_NUMBER%.zip -Force"'
                archiveArtifacts artifacts: 'dist/*.zip', fingerprint: true
            }
        }

        stage('Deploy') {
            steps {
                bat 'if not exist "%DEPLOY_DIR%" mkdir "%DEPLOY_DIR%"'
                bat 'copy /Y calculator.py "%DEPLOY_DIR%\\"'
                bat 'python "%DEPLOY_DIR%\\calculator.py" 5 7'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/results.xml'
        }
        success {
            echo 'Pipeline success: tests passed and deployed'
        }
        failure {
            echo 'Pipeline failed: check Console Output'
        }
    }
}
