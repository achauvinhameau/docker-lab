# -*- Mode: Python; python-indent-offset: 4 -*-
#
# Time-stamp: <2017-12-17 15:55:56 alex>
#
# --------------------------------------------------------------------
# Copyright (C) 2016-2017  Alexandre Chauvin Hameau <ach@meta-x.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

import sys
import os
import nose
import logging
import string
import json

sys.path.append(os.getcwd())

from ws_app import app
import ws_info, ws_prime


# ---------------------------------------------
def primeTest(i):
    """get result from web service"""
    global app

    c = app.test_client()

    rv = c.get("/check/{}".format(i))
    if rv.status_code != 200 and rv.status_code != 202:
        assert False, "error"

    j = json.loads(rv.data.decode())
    if j['status'] != "OK":
        assert False, "get /check failed"

    logging.info("{} {}".format(i, j['delay']))

    return j['result']


# ---------------------------------------------
def primeTestArray(iFrom, iTo, aPrime):
    """check 20 first numbers"""
    global app

    c = app.test_client()

    for i in range(iFrom, iTo):
        r = primeTest(i)
        if r and not i in aPrime:
            assert False, "get /check failed {} is not prime".format(i)

        if not r and i in aPrime:
            assert False, "get /check failed {} is prime".format(i)


# ---------------------------------------------
def test_1to20():
    """check 20 first numbers"""
    logging.info("check from 1 to 20")
    primeTestArray(1, 20, [2,3,5,7,11,13,17,19])


# ---------------------------------------------
def test_21to100():
    """check 20 to 100"""
    logging.info("check from 21 to 100")
    primeTestArray(21, 100, [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


def test_someBig():
    "test some Mersenne primes"
    logging.info("check primes from Mersenne primes")

    if not primeTest(131071):
        assert False, "131071 shoud be prime"

    if not primeTest(524287):
        assert False, "524287 shoud be prime"


def test_veryBig():
    "test some big Mersenne primes"
    logging.info("check big primes from Mersenne primes")
    return

    if not primeTest(2147483647):
        assert False, "2147483647 shoud be prime"

    if not primeTest(2305843009213693951):
        assert False, "2305843009213693951 shoud be prime"


# ---------------------------------------------
if __name__ == '__main__':
    _logFormat = '%(asctime)-15s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
    logging.basicConfig(format=_logFormat,
                        level=logging.INFO)

    test_1to20()
    test_21to100()
    test_someBig()
