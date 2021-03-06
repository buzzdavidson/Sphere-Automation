#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file is part of the B{Sphere Automation} project
(U{http://www.sphereautomation.org}).

B{Sphere Automation} - Open Home Automation for Linux
Copyright (C) 2011 Steve Davidson

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see U{http://www.gnu.org/licenses/}.

@author: Steve Davidson
@copyright: (C) 2011 Sphere Automation
@license: GPL(v3)
@organization: Sphere Automation
"""
from sphere.core.device import BaseSphereEntity

class BusException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)


class Bus(BaseSphereEntity):
    '''Represents a device bus within Sphere.  A device bus groups devices from a related technology, such as
    X10 devices.  A bus may optionally support device discovery.  A Bus will contain zero or more devices.'''

    def __init__(self, name = CoreEntity.UNKNOWN, description = CoreEntity.UNKNOWN):
        BaseSphereEntity.__init__(self, name, description)
        self._devices = list()
        self._busType = busType

    def enumerate(self):
        raise BusException("Must be overridden in implementing class")

class BusType(BaseSphereEntity):
    '''Represents a type of device bus within Sphere.'''
    def __init__(self, name=BusType.UNKNOWN, description=BusType.UNKNOWN):
        BaseSphereEntity.__init__(self, name, description)




