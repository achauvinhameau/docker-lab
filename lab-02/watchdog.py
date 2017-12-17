# -*- Mode: Python; python-indent-offset: 4 -*-
#
# Time-stamp: <2017-12-17 15:35:06 alex>
#
# --------------------------------------------------------------------

import logging
import time
import json
import redis
import os
import pprint
import psutil

dbRedisId = 1
dbHost = "localhost"
dbPort = 6379

if "OPS_REDIS_PORT" in os.environ:
    dbPort = os.environ['OPS_REDIS_PORT']
if "OPS_REDIS_HOST" in os.environ:
    dbHost = os.environ['OPS_REDIS_HOST']
if "OPS_REDIS_DB" in os.environ:
    dbRedisId = os.environ['OPS_REDIS_DB']


# --------------------------------------------
def redisConnect():
    """connects to the redis"""
    backOff = 1

    while True:
        logging.info("connect to redis {}:{}".format(dbHost, dbPort))

        db = redis.Redis(db=dbRedisId,
                         max_connections=1,
                         socket_timeout=2,
                         host=dbHost,
                         port=dbPort)

        try:
            db.ping()
            break

        except redis.ConnectionError as e:
            backOff *= 1.5
            if backOff > 30 or backOff < 0:
                db = None
                raise Exception('redis not running? abort')
            logging.error("redis : {}, next try in {:.2f}".format(e, backOff))
            time.sleep(backOff)

    return db

# ----------------------------------------

_logFormat = '%(asctime)-15s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
logging.basicConfig(format=_logFormat, level=logging.INFO)

# get the parameters from the configuration file
# reverts to default if not present
startTime = time.time()
iTimeout = 10
dAppInfo = {
    "name": "not set",
    "version": "not set",
    "date": {
        "start_s": time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(startTime)),
        "start": startTime
    },
    "watchdog": iTimeout,
    "hostname": os.environ['HOSTNAME'],
}

try:
    with open('/application.json') as json_data:
        d = json.load(json_data)
        if "name" in d:
            dAppInfo['name'] = d['name']
        if "version" in d:
            dAppInfo['version'] = d['version']
        if "watchdog" in d:
            w = int(d['watchdog'])
            w = min(300, w)
            w = max(10,w)
            iTimeout = w
            dAppInfo['watchdog'] = w

except IOError as e:
    logging.warning("cannot get /application.json file information")

iStartTime = time.time()

pprint.pprint(dAppInfo)

# connects to the redis server
db = redisConnect()

while True and db != None:
    dAppInfo['lastseen'] = time.time()
    dAppInfo['sys_pid'] = len(psutil.pids())
    dAppInfo['health-cpu'] = psutil.cpu_percent(interval=1, percpu=False)
    dAppInfo['uptime'] = int(time.time() - iStartTime)

    logging.info("set redis info for {}, sleep for {}".format(dAppInfo['hostname'], iTimeout/2))
    db.set(dAppInfo['hostname'], dAppInfo, ex=iTimeout)
    time.sleep(iTimeout/2)


""" exemple /application.json

{
"name": "prime",
"version": "1.2",
"watchdog": 60
}

"""
