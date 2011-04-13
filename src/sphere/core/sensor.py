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
from sphere.core.device import Device, DeviceType

class SensorException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)

class Sensor(Device):
    def __init__(self, sensorType = None):
        Device.__init__(self)
        self._sensorType = sensorType

class SensorType(DeviceType):
    def __init__(self, deviceCategory=DeviceType.UNKNOWN, name=DeviceType.UNKNOWN, description=DeviceType.UNKNOWN, dataType=None, units=None):
        DeviceType.__init__(self, deviceCategory, name, description)
        self._dataType = dataType
        self._units = units
        if self._deviceCategory is None or self._deviceCategory == DeviceType.UNKNOWN:
            self._deviceCategory = 'Sensor' # TODO: i18n

    dataType = property(lambda self: self._dataType)
    units = property(lambda self: self._units)

    # TODO: Unit handling and conversion
