docker build -t autogenstudio:latest autogenDocker


docker run -v ${PWD}/user/:/home/user/app/files/user/ -p 8081:8081/tcp autogenstudio:latest