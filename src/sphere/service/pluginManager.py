#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Plugin Manager

Responsibilities include:

- Plugin Lifecycle support (start, stop)
- Installation support (register, unregister, enable, disable)
- Plugin status reporting

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
import threading
from sphere.service.controllable import Controllable
from sphere.service.messenger import Messenger
from sphere.service.plumberjack import MessengerFactory, LogFactory

class PluginManager(Controllable):
    def __init__(self, configManager):
        Controllable.__init__(self, 'Plugin Manager')
        self._configManager = configManager
        self._pluginPath=None
        self._plugins=dict()
        self._messenger.subscribe(self, Messenger.TOPIC_COMPONENT_HEARTBEAT)
        # TODO: instantiate all plugins in plugin directory, but dont start
        # TODO: MANAGER controls enabled/disabled state: plugin has no idea
        # TODO: check plugin dependencies before starting or installing plugin

    def messengerCallback(self, topic, message):
        pass

    def _doStart(self):
        return True

    def _doStop(self):
        return True

    def getInstalledPlugins(self):
        return None

    def getAvailablePlugins(self, hideInstalled=False):
        return None

    def installPlugin(self, plugin):
        return None

    def uninstallPlugin(self, plugin):
        return None

    def controlPlugin(self, plugin, command):
        # command in start, stop, enable, disable
        # TODO call plugin initializePlugin
        return None

