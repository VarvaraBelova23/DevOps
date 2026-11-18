pipeline {
    agent any

    stages {
        stage('Подготовка окружения') {
            steps {
                echo 'Установка Docker, Docker Compose и клонирование репозитория...'
                ansiblePlaybook(
                    playbook: 'ansible/run_playbook.yml',
                    inventory: 'ansible/hosts',
                    tags: 'deploy',
                    colorized: true
                )
            }
        }

        stage('Запуск приложений') {
            steps {
                echo 'Запуск контейнеров через Docker Compose...'
                ansiblePlaybook(
                    playbook: 'ansible/run_playbook.yml',
                    inventory: 'ansible/hosts',
                    tags: 'up',
                    colorized: true
                )
            }
        }
    }
}
