pipeline {
    agent any
    stages {
        stage('git repo & clean') {
            steps {
               bat "rmdir  /s /q Inventory_management_system"
                bat "git clone https://github.com/Rajviradiyacoder4024/19it152.git"
                bat "mvn clean -f Inventory_management_system"
            }
        }
        stage('install') {
            steps {
                bat "mvn install -f Inventory_management_system"
            }
        }
        stage('test') {
            steps {
                bat "mvn test -f Inventory_management_system"
            }
        }
        stage('package') {
            steps {
                bat "mvn package -f Inventory_management_system"
            }
        }
    }
}
