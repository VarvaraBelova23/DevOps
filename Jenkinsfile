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