# Docker (Ubuntu18.04) for cgi with python 3.8

With this docker image, you can create simple web server with CGI.
(This is an adapted - stripped down - version, originally from Shohei Mukai)

## How to use

```bash
# build image
docker build -t pycgi .
# run image
HASH=`docker run -p 8883:80 -d pycgi`
# exec container
docker exec -it $HASH /bin/bash
```

OR: use convenience scripts `build.sh` and `run.sh`

You can access from the below URL after running the docker container.  

* Shell Script ... [http://localhost:8883/cgi-bin2/sh.cgi](http://localhost:8883/cgi-bin2/sh.cgi)
* Python3.8 ... [http://localhost:8883/cgi-bin2/py38.cgi](http://localhost:8883/cgi-bin2/py38.cgi)
(and some more)

### Original Licence

* [MIT](https://github.com/pyohei/docker-cgi-python/blob/master/LICENSE)
