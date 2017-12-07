# docker build -t prime .
# docker run --rm -p 5001:5000 -m 64m prime 

# source image, python 3
FROM python:latest

# me
MAINTAINER ach@meta-x.org

# copy reqs for python to be installed by pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy all python files to the container
COPY *py ./

EXPOSE 5000

# exec command at container start
CMD [ "python", "./srv.py", "-l", "INFO" ]
