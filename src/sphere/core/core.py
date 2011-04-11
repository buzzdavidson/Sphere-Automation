#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This file is part of the B{Sphere Automation} project 
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
from time import time
from enum import Enum

class CoreEntity():
    DATA_TYPES = Enum('String','Integer','Float','Boolean','Date','Binary')
    UNKNOWN = '(Unknown)'
    def __init__(self, name = CoreEntity.UNKNOWN, description = CoreEntity.UNKNOWN, location = CoreEntity.UNKNOWN):
        self._name = name
        self._location = location
        self._description = CoreEntity.UNKNOWN

    name = property(lambda self: self._name)
    location = property(lambda self: self._location)
    description = property(lambda self: self._description)

class Device(CoreEntity):
    DEVICE_STATUS = Enum('Unknown', 'New', 'Available', 'Missing', 'Error')
    def __init__(self):
        CoreEntity.__init__(self)
        self._address = None
        self._configuration = dict()
        self._status = Device.DEVICE_STATUS.Unknown
        self._lastUpdate = time.time()
        self._devices = list()
        
    address = property(lambda self: self._address)
    configuration = property(lambda self: self._configuration)
    status = property(lambda self: self._status)
    lastUpdate = property(lambda self: self._lastUpdate)
    devices = property(lambda self: self._devices)



    
    

