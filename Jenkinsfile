pipeline{
    agent any
    stages{
        stage('Setup Python Virtual ENV')
        {
            steps{
                sh '''
                chmod +x envsetup.sh
                ./envsetup.sh
                '''
            }
        }
        stage('uWSGI Setup')
        {
            steps{
                sh '''
                chmod +x uwsgi.sh
                ./uwsgi.sh
                '''
            }
        }
        stage('NGINX Setup')
        {
            steps{
                sh '''
                chmod +x nginx.sh
                ./nginx.sh
                '''
            }
        }
    }
}