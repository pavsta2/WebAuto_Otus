pipeline {
    agent any
    parameters {
        choice (
            name: "BROWSER",
            choices: 'chrome\nfirefox',
            description: "Browser name for autotests"
        )
        choice (
            name: "LOG_LEVEL",
            choices: 'INFO\nDEBUG',
            description: "Set log level"
        )
        choice (
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
        COMPOSE_FILE = 'compose.yml'
        TEST_IMAGE = 'autotests:latest'
        ALLURE_RESULTS = 'allure-results'
        }
        stages {
            stage('Prepare .env') {
                steps {
                    // Загружаем .env как файл в рабочую директорию
                    withCredentials([file(credentialsId: 'app-env-file', variable: 'ENV_FILE')]) {
                        sh '''
                        cp "$ENV_FILE" .env
                        chmod 600 .env
                        cat .env
                        '''
                    }
                }
            }
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
                    /usr/bin/docker build -t ${TEST_IMAGE} .
                    '''
                }
            }
            stage('Start Infrastructure: OpenCart & Selenoid') {
                steps {
                    sh '''
                    echo "Запуск OpenCart, БД, Selenoid и UI"
                    docker compose -f ${COMPOSE_FILE} up -d
                    '''
                }
            }
            stage('Run UI Tests with Parameters') {
                steps {
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        sh """
                        echo '=== Запуск автотестов с параметрами ==='
                        echo "BROWSER: ${params.BROWSER}"
                        echo "BROWSER_VER: ${params.BROWSER_VER}"
                        echo "REMOTE_URL: ${params.REMOTE_URL}"
                        echo "APP_URL: ${params.APP_URL}"
                        echo "WORKSPACE, куда монтируем рез-ты тестов: \$WORKSPACE"
                        echo "WORKSPACE: $WORKSPACE"
                        touch "$WORKSPACE/test_in_ws.txt" && echo "OK" || echo "FAIL"
                        ls -la "$WORKSPACE"

                        rm -rf "\$WORKSPACE/${ALLURE_RESULTS}"/*
                        mkdir -p "\$WORKSPACE/${ALLURE_RESULTS}"
                        chmod -R 777 "$WORKSPACE/${ALLURE_RESULTS}"
                        touch "$WORKSPACE/${ALLURE_RESULTS}/test_in_allure.txt" && echo "OK" || echo "FAIL"
                        ls -la "$WORKSPACE"/${ALLURE_RESULTS}

                        docker run --rm \\
                        -e BROWSER='${params.BROWSER}' \\
                        -e BROWSER_VER='${params.BROWSER_VER}' \\
                        -e REMOTE_URL='${params.REMOTE_URL}' \\
                        -e XDIST='${params.XDIST}' \\
                        -e APP_URL='${params.APP_URL}' \\
                        -e LOG_LEVEL='${params.LOG_LEVEL}' \\
                        -e ALLURE_RESULTS='/root/WebAuto_Otus/${ALLURE_RESULTS}' \\
                        --network selenoid3 \\
                        -v "jenkins_allure:/${ALLURE_RESULTS}" \\
                        ${TEST_IMAGE}
                        """
                    }
                }
            }
            stage('Fetch Allure Results') {
                steps {
                    sh '''
                    set -e
                    # Проверка 1: есть ли что-то в томе?
                    echo "Содержимое тома jenkins_allure:"
                    docker run --rm \
                    -v jenkins_allure:/check \
                    alpine ls -la /check

                    echo "=== Копируем результаты в WORKSPACE с помощью tar ==="
                    echo "WORKSPACE: $WORKSPACE"

                    # Создаём папку
                    mkdir -p "$WORKSPACE/allure-results"
                    cd "$WORKSPACE/allure-results"

                    # Архивируем содержимое тома jenkins_allure и распаковываем в текущую директорию
                    docker run --rm \
                    -v jenkins_allure:/data \
                    alpine \
                    tar -c -f - -C /data . | tar -x -f -
                    '''
                    # Делаем файлы доступными
                    chmod -R 777 "$WORKSPACE/allure-results"

                    echo "=== Содержимое WORKSPACE/allure-results ==="
                    ls -la "$WORKSPACE/allure-results"
                    '''
                }
            }
            stage('Generate Allure Report') {
                steps {
                    script {
                        allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: './allure-results']]
                        ])
                    }
                }
            }

        }
}