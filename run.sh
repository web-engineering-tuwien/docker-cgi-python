# run image

NAME=cgi-server

# exec container
docker run --name ${NAME} -p 8883:80 -d \
	-v cgi-bin:/production/www/cgi-bin \
		pycgi
     
