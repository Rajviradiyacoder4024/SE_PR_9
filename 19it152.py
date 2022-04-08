pipeline {
    agent any
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
