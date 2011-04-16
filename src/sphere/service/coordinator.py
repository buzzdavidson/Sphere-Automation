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
import controller
from sphere.service.configManager import ConfigManager
from sphere.service.controllable import Controllable, startComponent
from sphere.service.deviceRegistry import DeviceRegistry
from sphere.service.deviceManager import DeviceManager
from sphere.service.messenger import Messenger
from sphere.service.messenger.simpleMessenger import SimpleMessenger
from sphere.service.pluginManager import PluginManager
from sphere.service.plumberjack import LogFactory, MessengerFactory

class SphereCoordinator(Controllable):
    ''' This is the central component of Sphere.  Responsibilities include Global lifecycle support
    (startup, shutdown, etc), Coordination between application components
    '''
    def __init__(self):
        Controllable.__init__(self, 'Coordinator')
        self._components = list()
        MessengerFactory._messenger = SimpleMessenger() # TODO: configure this properly (directly in plumberjack)
        configManager = ConfigManager()
        self._components.append(configManager)
        self._components.append(PluginManager(configManager))
        self._components.append(DeviceManager(configManager))
        self._loopInterval = 1

    runLoopInterval = property(lambda self: self._loopInterval)

    def messengerCallback(self, topic, message):
        pass

    def _doStart(self):
        startcount = 0
        for component in self._components:
            startComponent(component)
            if component.status == Controllable.STATUS.Started:
                startcount += 1
        retval = (startcount == len(self._components))
        self._log.debug('Started %d of %d registered components [%s]', startcount, len(self._components), retval)
        return retval

    def _doStop(self):
        stopcount = 0
        for component in reversed(self._components):
            startComponent(component)
            if component.status == Controllable.STATUS.Stopped:
                stopcount += 1
        retval = (stopcount == len(self._components))
        self._log.debug('Stopped %d of %d registered components [%s]', stopcount, len(self._components), retval)
        return retval

    def run(self):
        while(True):
            for component in self._components:
                component.refresh()
            time.sleep(self._loopInterval)
