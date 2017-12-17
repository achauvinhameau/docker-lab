# -*- Mode: Python; python-indent-offset: 4 -*-
#
# Time-stamp: <2017-12-07 16:06:35 alex>
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
 web service for prime number checker
"""

import logging
from flask import Flask

# ----------- parse args
try:
    import argparse
    parser = argparse.ArgumentParser(description='prime checker')

    parser.add_argument('--log', '-l', metavar='level', default='ERROR', type=str, help='log level DEBUG, INFO, WARNING, ERROR', nargs=1, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'])
    parser.add_argument('--debug', '-d', help='debug mode for engine',
                        action='store_true')

    args = parser.parse_args()

except ImportError:
    log.error('parse error')
    exit()

if not isinstance(args.debug, bool):
    logging.error('debug arg is not taking argument')
    exit()

# ----- set the log level and format
_logFormat = '%(asctime)-15s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
logLevel = logging.ERROR

if args.log[0] == 'DEBUG':
    logLevel = logging.DEBUG
if args.log[0] == 'WARNING':
    logLevel = logging.WARNING
if args.log[0] == 'ERROR':
    logLevel = logging.ERROR
if args.log[0] == 'INFO':
    logLevel = logging.INFO

logging.basicConfig(format=_logFormat, level=logLevel)

from ws_app import app
import ws_info
import ws_prime

if __name__ == '__main__':
    logging.info("starting prime server")

    app.debug = args.debug
    app.secret_key = "prime-checker"
    app.run(host='0.0.0.0')
