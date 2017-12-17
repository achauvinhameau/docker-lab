# -*- Mode: Python; python-indent-offset: 4 -*-
#
# Time-stamp: <2017-12-10 16:22:38 alex>
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
 information module
"""

from ws_app import app
from flask import make_response, jsonify, request


@app.route('/info')
def ws_info():
    """
    / ws : provides information
    """
    return make_response(jsonify({
        'status': 'OK',
        'name': 'prime checker',
        'version': 1
    }), 200)


@app.errorhandler(404)
def not_found(error):
    """
    handle the 404 error
    """
    return make_response(jsonify({'error': 'Not found'}), 404)
