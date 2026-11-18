pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                echo 'Запуск развертывания через Ansible...'
                dir('ansible') {
                    ansiblePlaybook(
                        playbook: 'run_playbook.yml',
                        tags: 'deploy',
                        colorized: true
                    )
                }
            }
        }
        stage('Stop') {
            steps {
                echo 'Остановка контейнеров...'
                dir('ansible') {
                    ansiblePlaybook(
                        playbook: 'run_playbook.yml',
                        tags: 'stop',
                        colorized: true
                    )
                }
            }
        }
    }
}