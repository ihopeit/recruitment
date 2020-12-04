pipeline {
  agent any
  stages {
    stage('Checkout Source') {
      steps {
        git url:'https://gitee.com/geektime-geekbang/django.git', branch:'master'
      }
    }
    
    stage('Docker Build') {
      steps {
        sh "docker build -t ihopeit/django-recruitment:${env.BUILD_NUMBER} ."
        sh "docker tag ihopeit/django-recruitment:${env.BUILD_NUMBER} registry.cn-beijing.aliyuncs.com/ihopeit/django-recruitment:${env.BUILD_NUMBER}"
      }
    }
    stage('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'aliyunhub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword} registry.cn-beijing.aliyuncs.com"
          sh "docker push registry.cn-beijing.aliyuncs.com/ihopeit/django-recruitment:${env.BUILD_NUMBER}"
        }
      }
    }
    stage('Docker Remove Image') {
      steps {
        sh "docker rmi registry.cn-beijing.aliyuncs.com/ihopeit/django-recruitment:${env.BUILD_NUMBER}"
        sh "docker rmi ihopeit/django-recruitment:${env.BUILD_NUMBER}"
      }
    }
    stage('Apply Kubernetes Files') {
      steps {
          withKubeConfig([credentialsId: 'kubeconfig']) {
          sh 'kubectl apply -f k8s/web-claim0-persistentvolumeclaim.yaml '
          sh 'kubectl apply -f k8s/redis-service.yaml'
          sh 'kubectl apply -f k8s/flower-service.yaml'
          sh 'kubectl apply -f k8s/web-service.yaml'
          sh 'kubectl apply -f k8s/redis-deployment.yaml'
          
          sh 'cat k8s/celery-deployment.yaml | sed "s/{{BUILD_NUMBER}}/$BUILD_NUMBER/g" | kubectl apply -f -'
          sh 'cat k8s/flower-deployment.yaml | sed "s/{{BUILD_NUMBER}}/$BUILD_NUMBER/g" | kubectl apply -f -'
          sh 'cat k8s/web-deployment.yaml    | sed "s/{{BUILD_NUMBER}}/$BUILD_NUMBER/g" | kubectl apply -f -'
        }
      }
    }
  }
  post {
    success {
      sh "echo Pipeline is successfully completed."
    }
    failure {
      sh "echo Pipeline failed. Please check the logs."
    }
  }
}