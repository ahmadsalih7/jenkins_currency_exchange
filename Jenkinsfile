pipeline {
	agent any
	stages {
		stage('Build'){
			steps {
				echo "Build"
			}
		}
		stage('Test'){
			steps {
				echo "Test"
			}
		}
		stage('Integration Test'){
			steps {
				echo "Integration Test"
			}
		}
	}
	post {
		always {
			echo "I always run"
		}
		success {
			echo "I run only if you success"
		}
		failure {
			echo "I run when you fail"
		}
	}
}
