pipeline {
    agent any

    options {
        buildDiscarder logRotator( 
                    daysToKeepStr: '16', 
                    numToKeepStr: '10'
            )
    }

    environment {
        app_repo    = "https://shashikant09@github.com/shashikant09/dataproc-cicd.git"
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
                git branch: 'master', url: "${env.app_repo}"
            }
        stage('Run gcloud') {
            steps {
                withEnv(['GCLOUD_PATH=/usr/bin']) {
                sh '$GCLOUD_PATH/gsutil cp ./gcs-dataproc-bigquery.py gs://us-central1-demo-ephemeral--c797ec6a-bucket/dags/
            }
         }
      }
   }
}



