pipeline {
	// agent {docker {image 'ahmadsalih7/my_flask_image:0.0.0'} }
	agent any
	environment {
		dockerHome = tool 'myDocker'
		PATH = "dockerHome/bin:$PATH"
	}
	stages {
		stage('Build'){
			steps {
				sh "docker version"
				echo "Build"
				echo " PATH $PATH"
				echo "BUILD_NUMBER $env.BUILD_NUMBER"
				echo "BUILD_TAG $env.BUILD_TAG"
				echo "BUILD_ID $env.BUILD_ID"
				echo "BUILD_URL $env.BUILD_URL"
				echo "JOB_NAME $env.JOB_NAME"

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
