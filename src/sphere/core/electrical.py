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
from sphere import CoreEntity
from sphere.common.enum import Enum
from sphere.core.bus import Bus
from sphere.core.device import BaseSphereEntity, Device

class Circuit(Bus):
    '''A Simple Device Bus representing a household electrical circuit.  May be useful for modeling the electrical system
    within a house, in order to catalog the devices (outlets, lights, switches, etc) on a single circuit breaker.'''
    def __init__(self):
        Bus.__init__(self)

class ElectricalDevice(Device):
    '''Represents a single household electrical device, such as an outlet, a circuit breaker, or a light.'''
    def __init__(self):
        Device.__init__(self)
        self._deviceType = "Electrical"
