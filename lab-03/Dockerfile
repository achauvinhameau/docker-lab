# lab 03
#
# docker build -t prime:1 .
# docker run --rm -p 5001:5000 -m 64m prime

# source image ops-python
FROM ops-python:latest

# me
MAINTAINER ach@meta-x.org

# copy reqs for python to be installed by pip
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# copy all python files to the container
COPY *py application.json start.sh /

EXPOSE 5000
