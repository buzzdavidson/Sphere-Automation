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

class PluginException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)

class Plugin(Controllable):
    def __init__(self, name):
        Controllable.__init__(self, name)
        self._deviceRegistry = None
        self._configuration = None

    def initializePlugin(self, deviceRegistry):
        self._deviceRegistry = deviceRegistry
        self._registerDeviceMetadata()

    def messengerCallback(self, topic, message):
        pass

#    def _doStart(self):
#        return True
#
#    def _doStop(self):
#        return True

    def _registerDeviceMetadata(self):
        self._log.debug('Device [%s] does not register device metadata', self._getName())



