#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
messenger provides an abstraction layer for a pub/sub message bus.  Clients work with messenger directly, and
plumberjack wires the appropriate implementation in to the system.

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
from abc import ABCMeta, abstractmethod

class Messenger():
    __metaclass__ = ABCMeta
    TOPIC_SYSTEM = 'system'
    TOPIC_SYSTEM_CONTROL = 'system.control'
    TOPIC_COMPONENT_STATUS = 'component.status'
    TOPIC_COMPONENT_HEARTBEAT = 'component.heartbeat'

    # implementations look for: def messengerCallback(self, topic, message):

    @abstractmethod
    def publish(self, topic, message):
        pass

    @abstractmethod
    def subscribe(self, topic, callback=None):
        pass

    
