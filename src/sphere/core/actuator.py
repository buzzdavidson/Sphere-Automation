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
from sphere.core.device import Device, DeviceType

class ActuatorException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value
    def __str__(self):
        return repr(self.value)

class Actuator(Device):
    '''Represents a single Actuator device within Sphere.  An Actuator is any device which effects its
    environment, such as a switch or relay.  The read-only equivalent of an Actuator is a Sensor.
    Actuators in Sphere are fine-grained objects; a device which affects several items, such as a
    relay board with several relays, would be modeled as a device with one actuator for each relay.'''
    def __init__(self):
        Device.__init__(self)
        self._sensorType = sensorClass

class ActuatorType(DeviceType):
    '''Represents a single type of actuator within sphere'''
    def __init__(self, deviceCategory=DeviceType.UNKNOWN, name=DeviceType.UNKNOWN, description=DeviceType.UNKNOWN, dataType=None, allowedStates=None):
        DeviceType.__init__(self, deviceCategory, name, description)
        self._allowedStates = allowedStates
        self._dataType = dataType
        if self._deviceCategory is None:
            self._deviceCategory = 'Actuator' # TODO: i18n

    allowedStates = property(lambda self: self._allowedStates)
    dataType = property(lambda self: self._dataType)
