pipeline {
    agent any

    options {
        buildDiscarder logRotator( 
                    daysToKeepStr: '16', 
                    numToKeepStr: '10'
            )
    }

    environment {
        app_repo    = "https://github.com/shashikant09/dataproc-cicd.git"
        PROJECT_ID = 'broadcom-service-project2'          
    }

    stages {
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
                sh """
                echo "Cleaned Up Workspace For Project"
                """
            }
        }

//        stage('Code Checkout') {
//            steps {
//               checkout([
//                    $class: 'GitSCM', 
//                   branches: [[name: '*/*']], 
//                   userRemoteConfigs: [[url: 'https://github.com/dobbster/dataproc-test.git']]
//               ])
//           }
//       }

        stage('Build') {
            steps {
                git branch: 'main', url: "${env.app_repo}"
                }
        }
        stage('Run gcloud') {
            steps {
                withEnv(['GCLOUD_PATH=/usr/bin']) {
                sh 'echo $BUILD_ID'
                sh 'echo $PROJECT_ID'
                sh 'echo $BUILD_NUMBER'
//                sh '$GCLOUD_PATH/gcloud composer environments update demo-ephemeral-dataproc --project=$PROJECT_ID --location=us-central1 --update-env-variables=BUILD_ID=$BUILD_ID'
                sh 'sudo apt-get install kubectl'
                sh '$GCLOUD_PATH/gcloud composer environments run demo-ephemeral-dataproc --project=$PROJECT_ID --location=us-central1 variables -- --set BUILD_ID $BUILD_ID'
                sh '$GCLOUD_PATH/gsutil cp ./example-build.py gs://us-central1-demo-ephemeral--c797ec6a-bucket/dags/'
            }
         }
      }
   }
}
