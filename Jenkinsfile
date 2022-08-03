pipeline {
	agent {docker {image 'ahmadsalih7/my_flask_image:0.0.0'} }
	stages {
		stage('Build'){
			steps {
				sh 'flask --version'
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
