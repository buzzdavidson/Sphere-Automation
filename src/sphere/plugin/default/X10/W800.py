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
from sphere.core.bus import BusType
from sphere.core.device import DeviceType
from sphere.plugin.core.plugin import Plugin
from sphere.plugin.core.serialListenerPlugin import SerialListenerPlugin

class W800(SerialListenerPlugin):
    def __init__(self):
        SerialListenerPlugin.__init__(self, 'W800')
        self._description = 'Plugin to support WGL W800 X10 RF Receiver'
        self._version = '0.1.0'
        self._requirements.append('coreX10 >= 0.1.0')

    def _doStart(self):
        return True

    def _doStop(self):
        return True

    def _registerDeviceMetadata(self):
        self._deviceManager.registerDeviceType(DeviceType(deviceCategory='Interface', name='W800RF', description='W800 X10 RF Receiver', busType='X10'))

    def _loadConfiguration(self, configManager):
        pass
