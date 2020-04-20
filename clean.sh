# clean up Docker container
NAME=cgi-server

docker stop ${NAME}
docker rm ${NAME}

