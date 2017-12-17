# lab-02
# python image to be used by devs to prepare the packages
#
#
# docker build -t ops-python:1 .
# docker run --rm -m 64m ops-python

# source image, python 3
FROM centos:7

# me
MAINTAINER ach@meta-x.org

RUN yum -y install epel-release && yum -y install python34 python34-setuptools python34-scipy python34-numpy python34-simplejson && yum -y group install "Development Tools" && easy_install-3.4 pip && pip install redis && pip install psutil && yum -y group remove "Development Tools"  && yum -y remove perl

COPY watchdog.py /
COPY ops-start.sh /

CMD [ "bash", "/ops-start.sh" ]
