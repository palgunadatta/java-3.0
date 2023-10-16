@Library('my-shared-library') _

pipeline{

    agent any

    parameters{

        choice(name: 'action', choices: 'create\ndelete', description: 'Choose create/Destroy')
        string(name: 'ImageName', description: "name of the docker build", defaultValue: 'javapp')
        string(name: 'ImageTag', description: "tag of the docker build", defaultValue: 'v1')
        string(name: 'DockerHubUser', description: "name of the Application", defaultValue: 'praveensingam1994')
    }

    stages{
         
        stage('Git Checkout'){
                    when { expression {  params.action == 'create' } }
            steps{
            gitCheckout(
                branch: "main",
                url: "https://github.com/praveen1994dec/Java_app_3.0.git"
            )
            }
        }
         stage('Unit Test maven'){
         
         when { expression {  params.action == 'create' } }

            steps{
               script{
                   
                   mvnTest()
               }
            }
        }
         stage('Integration Test maven'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   mvnIntegrationTest()
               }
            }
        }
       //  stage('Static code analysis: Sonarqube'){
       //   when { expression {  params.action == 'create' } }
       //      steps{
       //         script{
                   
       //             def SonarQubecredentialsId = 'sonarqube-api'
       //             statiCodeAnalysis(SonarQubecredentialsId)
       //         }
       //      }
       // }
       // stage('Quality Gate Status Check : Sonarqube'){
       //   when { expression {  params.action == 'create' } }
       //      steps{
       //         script{
                   
       //             def SonarQubecredentialsId = 'sonarqube-api'
       //             QualityGateStatus(SonarQubecredentialsId)
       //         }
       //      }
       // }
        stage('Maven Build : maven'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   mvnBuild()
               }
            }
        }
        // stage('Push JAR file to Jfrog repo : python script'){
        //  when { expression {  params.action == 'create' } }
        //     steps{
        //        script{
                   
        //            jarpush()
        //        }
        //     }
        // }
        stage('Jar push JFROG : jfrog'){
        when { expression { params.action == 'create' } }
        steps{
            script{
                def artifactoryUrl = 'http://54.208.122.242:8082/artifactory'
                def artifactoryRepo = 'example-repo-local'
                def jarFileName = 'kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
                def targetPath = "${artifactoryRepo}/home/"
                sh """
                cd /var/lib/jenkins/workspace/assmnt2/target/
                chmod +x ${jarFileName}
                curl -X PUT -u admin:palgunadatta -T ${jarFileName} ${artifactoryUrl}/${targetPath}
                """
                }
            }
        }
        stage('Docker Image Build'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerBuild("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }
         stage('Docker Image Scan: trivy '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImageScan("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }
        stage('Docker Image Push : DockerHub '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImagePush("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }   
        stage('Docker Image Cleanup : DockerHub '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImageCleanup("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }      
    }
}
