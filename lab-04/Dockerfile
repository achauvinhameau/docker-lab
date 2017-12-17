# docker build -t prime-tests .
# docker run --rm -m 64m prime-tests

# source image, python 3
FROM prime:homolo

# me
MAINTAINER ach@meta-x.org

# copy reqs for python to be installed by pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy all python files to the container
COPY *py tests/

# exec command at container start
CMD [ "nosetests", "-v", "./tests"]
