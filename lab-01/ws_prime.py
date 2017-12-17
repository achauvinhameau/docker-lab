# -*- Mode: Python; python-indent-offset: 4 -*-
#
# Time-stamp: <2017-12-10 15:31:52 alex>
#
# --------------------------------------------------------------------
# docker-lab-01 - prime number checker ws
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

"""
 prime module
"""

import logging
from datetime import datetime

from ws_app import app
from flask import make_response, jsonify, request
from isPrime import *


@app.route('/check/<int:iToCheck>', methods=['GET'])
def ws_check(iToCheck):
    """
    / ws : check if int number passed is a prime
    """

    logging.debug("check if prime i={}".format(iToCheck))

    bmillis = datetime.now().microsecond
    r = isPrime(iToCheck)

    amillis = datetime.now().microsecond
    iReturnCode = 200
    if not r:
        iReturnCode = 202

    return make_response(jsonify({
        'status': 'OK',
        'number': iToCheck,
        'result': r,
        'delay': amillis - bmillis
    }), iReturnCode)
