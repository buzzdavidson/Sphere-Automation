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
from sphere.service.controllable import Controllable, ControllableException

class PluginException(ControllableException):
    def __init__(self, value):
        ControllableException.__init__(self, value)
        self.value = value

    def __str__(self):
        return repr(self.value)

class Plugin(Controllable):
    '''Basic plugin component'''

    def __init__(self, name):
        Controllable.__init__(self, name)
        self._deviceManager = None
        self._configuration = None
        self._requirements = list()
        self._version = None

    def initializePlugin(self, configManager, deviceManager):
        '''Called by PluginManager when loaded to allow plugins to load configuration and prepare themselves
         for execution.  Plugins should not enter a run loop or do any heavy processing during the execution
         of this method.'''
        self._deviceManager = deviceManager
        self._registerDeviceMetadata()
        self._loadConfiguration(configManager)
        # TODO: assert that properties are set

    def messengerCallback(self, topic, message):
        pass

    def _registerDeviceMetadata(self):
        '''Called by PluginManager when loaded to allow plugins to register any device metadata (bus types,
        device types, etc) prior to execution.'''
        self._log.debug('Device [%s] does not register device metadata', self._name)

    def _loadConfiguration(self, configManager):
        '''Called by PluginManager when loaded to allow plugins to load their configuration data from the
        supplied configManager instance'''
        self._log.debug('Device [%s] does not load device configuration', self._name)

