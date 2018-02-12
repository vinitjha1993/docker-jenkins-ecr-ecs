node {
    def app
   
    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        steps {
                sh "docker-compose up -d"
                }

        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("r-v-repo")
    }


    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
        docker.withRegistry('https://649347328056.dkr.ecr.us-west-2.amazonaws.com/r-v-repo', 'ecr:us-west-2:docker-jenkins-ecr') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
