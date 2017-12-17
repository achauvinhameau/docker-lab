# -*- Mode: Python; python-indent-offset: 4 -*-
#
# Time-stamp: <2017-12-10 15:21:36 alex>
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
 prime checker module
"""

import logging

def isPrime(i):
    """checks wether i is prime"""

    if i <= 1:
        return False

    if i <= 3:
        return True

    if i % 2 == 0 or i % 3 == 0:
        return False

    return True


def isPrimev2(i):
    """checks wether i is prime"""

    if i <= 1:
        return False

    if i <= 3:
        return True

    if i % 2 == 0:
        return False

    bFlag = True
    j = 3
    while j < i:
        if i % j == 0:
            return False
        j += 2

    return bFlag


aPrime = [2,3]

def isPrimev3(i):
    """checks wether i is prime"""

    logging.debug(aPrime)

    if i <= 1:
        return False

    if i <= 3:
        return True

    for p in aPrime:
        if i % p == 0:
            return False

    if len(aPrime) < 1000:
        aPrime.append(i)

    return True
