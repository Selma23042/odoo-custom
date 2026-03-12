pipeline {
    agent any

    environment {
        IMAGE_NAME = "odoo-custom"
        NEXUS_URL  = "nexus:8082"
        STAGING_NS = "staging"
        PROD_NS    = "production"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verification Syntaxe Python') {
            steps {
                sh '''
            python3 -m venv .venv
            .venv/bin/pip install flake8 --quiet
            .venv/bin/flake8 . --max-line-length=120 --exclude=.venv
        '''
    } 
     
        }

        stage('Tests Unitaires') {
            steps {
       sh '''
            python3 -m venv .venv
            .venv/bin/pip install pytest --quiet
            .venv/bin/pytest addons/module_test_devops/tests/ -v
        '''
    }
        }

        stage('Analyse SonarQube') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner -Dsonar.projectKey=odoo-custom'
                }
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Build Image Docker') {
            steps {
                sh """
                    docker build \
                      -t ${NEXUS_URL}/${IMAGE_NAME}:${BUILD_NUMBER} .
                """
            }
        }

        stage('Scan Securite Trivy') {
            steps {
                sh """
                    trivy image --exit-code 1 \
                      --severity HIGH,CRITICAL \
                      ${NEXUS_URL}/${IMAGE_NAME}:${BUILD_NUMBER}
                """
            }
        }

        stage('Push vers Nexus') {
            steps {
                sh "docker push ${NEXUS_URL}/${IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }

        stage('Deploy Staging') {
            steps {
                sh """
                    helm upgrade --install odoo-staging ./helm \
                      --namespace ${STAGING_NS} \
                      --set image.tag=${BUILD_NUMBER} \
                      --atomic --wait
                """
            }
        }

        stage('Tests Validation Staging') {
            steps {
                sh 'sleep 20'
                sh 'curl -f http://odoo-staging:8070/web/health'
            }
        }

        stage('Deploy Production') {
            when { branch 'main' }
            steps {
                sh """
                    helm upgrade --install odoo-prod ./helm \
                      --namespace ${PROD_NS} \
                      --set image.tag=${BUILD_NUMBER} \
                      --atomic --wait
                """
            }
        }
    }

    post {
        success {
            echo "✅ Build ${BUILD_NUMBER} déployé avec succès !"
 }
        failure {
            echo "❌ Build ${BUILD_NUMBER} échoué !" 
               sh """
                helm rollback odoo-staging \
                  --namespace ${STAGING_NS} || true
            """
        }
    }
}