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
from core import CoreEntity
from core import Device

class ActuatorException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)

class Actuator(Device):
    def __init__(self, actuatorClass = None, sensorClass = None):
        CoreEntity.__init__(self)
        self._actuatorClass = actuatorClass
        self._sensorClass = sensorClass

class ActuatorType():
    def __init__(self, name = CoreEntity.UNKNOWN, description = CoreEntity.UNKNOWN, dataType = CoreEntity.DATA_TYPES.String, allowedStates = None):
        self._name = name
        self._description = description
        self._dataType = dataType
        self._allowedStates = allowedStates

    name = property(lambda self: self._name)
    dataType = property(lambda self: self._dataType)
    description = property(lambda self: self._description)
    allowedStates = property(lambda self: self._allowedStates)
