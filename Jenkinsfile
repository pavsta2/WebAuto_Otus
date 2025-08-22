pipeline {
    agent any
    parameters {
        choices (
            name: "BROWSER",
            choices: 'chrome\nfirefox',
            description: "Browser name for autotests"
        )
        choices (
            name: "LOG_LEVEL",
            choices: 'INFO\nDEBUG',
            description: "Set log level"
        )
        choices (
            name: "BROWSER_VER",
            choices: '128.0\n127.0',
            description: "Set browser version"
        )
        string (
            name: "XDIST",
            defaultValue: '2',
            description: "Set a number of workers"
        )
        string (
            name: "REMOTE_URL",
            defaultValue: 'http://selenoid3:4444/wd/hub',
            description: "Remote url"
        )
        }
        environment {
        COMPOSE_FILE = 'docker-compose_jen.yml'
        TEST_IMAGE = 'autotests:latest'
        ALLURE_RESULTS = 'allure-results'
        }
        stages {
            stage('Checkout from GitHub') {
                steps {
                    git branch: 'homework_jenkins',
                        url: 'https://github.com/pavsta2/WebAuto_Otus.git'
                }
            }
            stage('Build Test Image with Fresh Code') {
                steps {
                    sh '''
                    echo "Сборка образа с тестами"
                    docker build -t ${TEST_IMAGE} .
                    '''
                }
            }
            stage('Start Infrastructure: OpenCart & Selenoid') {
                steps {
                    sh '''
                    echo "Запуск OpenCart, БД, Selenoid и UI"
                    docker-compose -f ${COMPOSE_FILE} up -d
                    '''
                }
            }
            stage('Wait for OpenCart to be Ready') {
                steps {
                    script {
                        timeout(time: 5, unit: 'MINUTES') {
                            waitUntil {
                                script {
                                    def status = sh(
                                        script: "curl -f -s -o /dev/null http://localhost:8081 || exit 1",
                                        returnStatus: true
                                    )
                                    return status == 0
                                }
                            }
                        }
                    }
                }
            }
            stage('Run UI Tests with Parameters') {
                steps {
                    sh """
                    echo '=== Запуск автотестов с параметрами ==='
                    echo "BROWSER: ${params.BROWSER}"
                    echo "BROWSER_VER: ${params.BROWSER_VER}"
                    echo "REMOTE_URL: ${params.REMOTE_URL}"
                    echo "APP_URL: ${params.APP_URL}"

                    docker run --rm \\
                    -e BROWSER='${params.BROWSER}' \\
                    -e BROWSER_VER='${params.BROWSER_VER}' \\
                    -e REMOTE_URL='${params.REMOTE_URL}' \\
                    -e APP_URL='${params.APP_URL}' \\
                    -e LOG_LEVEL='${params.LOG_LEVEL}' \\
                    -e ALLURE_RESULTS='${ALLURE_RESULTS}' \\
                    --network selenoid3 \\
                    -v \$(pwd)/${ALLURE_RESULTS}:/app/${ALLURE_RESULTS} \\
                    ${TEST_IMAGE}
                    """
                }
            }
        }
}