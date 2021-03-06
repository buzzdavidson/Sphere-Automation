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
from sphere.service.controllable import Controllable

class DeviceManager(Controllable):
    '''DeviceManager is the central registry for devices and device-related metadata.'''

    def __init__(self, configManager):
        Controllable.__init__(self, 'Device Registry')
        self._configManager = configManager

    def registerDeviceCategory(self, deviceCategory):
        '''Register a category of devices'''
        pass

    def registerDeviceType(self, type):
        '''Register a new device type'''
        pass

    def registerDevice(self, device):
        '''Register a new device'''
        pass

    def getDevicesOfType(self, type):
        '''Retrieve a list of devices by device type'''
        pass

    def getDevicesOfCategory(self, type):
        '''Retrieve a list of devices by device category'''
        pass

    def getDevice(self, id):
        '''Retrieve device node'''
        pass

    def registerBusType(self, type):
        '''Register a new bus type'''
        pass


