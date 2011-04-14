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

import logging
import threading
from time import time
from sphere.service.configManager import ConfigManager
from sphere.service.controllable import Controllable
from sphere.service.deviceRegistry import DeviceRegistry
from sphere.service.messenger import Messenger
from sphere.service.messenger.simpleMessenger import SimpleMessenger
from sphere.service.pluginManager import PluginManager
from sphere.service.plumberjack import LogFactory, MessengerFactory

class SphereCoordinator(Controllable):
    ''' This is the central component of Sphere.  Responsibilities include Global lifecycle support
    (startup, shutdown, etc), Coordination between application components
    '''
    def __init__(self):
        '''Global State Variables - key=varname, value=string'''
        Controllable.__init__(self, 'Coordinator')
        MessengerFactory._messenger = SimpleMessenger() # TODO: configure this properly (directly in plumberjack)
        self._globalState=dict()
        self._configManager = ConfigManager()
        self._pluginManager = PluginManager(self._configManager)
        self._deviceRegistry = DeviceRegistry(self._configManager)

    runLoopInterval = property(lambda self: self._loopInterval)

    def messengerCallback(self, topic, message):
        pass

    def _doStart(self):
        self._configManager.start()
        self._deviceRegistry.start()
        self._pluginManager.start()
        return self._pluginManager.status == Controllable.STATUS.Started

    def _doStop(self):
        # TODO: stop all children
        pass
