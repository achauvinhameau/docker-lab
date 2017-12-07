# -*- Mode: Python; python-indent-offset: 4 -*-
#
# Time-stamp: <2017-12-07 15:27:35 alex>
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
 flask app
"""

__version__ = "1.0"
__date__ = "07/12/2017"

from flask import Flask
app = Flask(__name__)
