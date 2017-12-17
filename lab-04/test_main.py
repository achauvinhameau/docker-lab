# -*- Mode: Python; python-indent-offset: 4 -*-
#
# Time-stamp: <2017-12-17 15:55:44 alex>
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
def test_main():
    """get /"""
    global app

    c = app.test_client()
    # get /
    rv = c.get("/")
    if rv.status_code != 404:
        assert False, "get / should failed"


# ---------------------------------------------
def test_404():
    """get 404"""
    global app

    c = app.test_client()

    # get /unknown
    rv = c.get("/unknown")
    if rv.status_code != 404:
        assert False, "404 expected"


# ---------------------------------------------
def test_info():
    """get info"""
    global app

    c = app.test_client()

    # get /info
    rv = c.get("/info")
    if rv.status_code != 200:
        assert False, "200 expected"

    j = json.loads(rv.data.decode())
    if j['status'] != "OK":
        assert False, "get /info failed"


# ---------------------------------------------
if __name__ == '__main__':
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)

    _logFormat = '%(asctime)-15s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
    logging.basicConfig(format=_logFormat,
                        level=logging.DEBUG)

    logging.info("starting")

    test_main()
    test_404()
    test_info()
