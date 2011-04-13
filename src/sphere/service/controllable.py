#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ABC for controllable components (components with start/stop functionality)
Adds basic features common to these components - lifecycle management,
logging, and messenger

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
import threading
from sphere.common.enum import Enum
from sphere.service.messenger import Messenger
from sphere.service.plumberjack import MessengerFactory, LogFactory

class ControllableException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)

class Controllable:
    __metaclass__ = ABCMeta

    STATUS = Enum('Unknown','Starting','Started','Stopping','Stopped','Error')

    def __init__(self, name):
        self._status = Controllable.STATUS.Unknown
        self._messenger = MessengerFactory.getMessenger(self, self)
        self._log = LogFactory.getLogger(self, self)
        self._stop = threading.Event()
        self._name = name
        self._description = None
        self._messenger.subscribe(Messenger.TOPIC_SYSTEM_CONTROL)
        # TODO: subscribe to necessary system topics

    @abstractmethod
    def _doStart(self):
        '''Start the component's processing.  Should perform actual startup.
          Base class takes care of logging, messaging, and state change.
          Must return boolean indicating success of operation.
          Implementing classes should throw ControllableException on error.'''
        pass

    def start(self):
        '''Perform actual startup, wraps call to _doStart.  This method takes care of clearing the self._stop event.
        There is little benefit to overriding this method.'''
        if self._status in (Controllable.STATUS.Unknown,Controllable.STATUS.Stopped,Controllable.STATUS.Error):
            self._setStatus(Controllable.STATUS.Starting)
            try:
                self._log.debug("Starting component [%s]...", self._name())
                self._stop.clear()
                stat = self._doStart()
                if stat:
                    self._log.debug("Component [%s] started.", self._name())
                else:
                    self._log.warning("Unable to start component [%s]!", self._name())
                newStatus = Controllable.STATUS.Started if stat else Controllable.STATUS.Stopped
                self._setStatus(newStatus)
            except ControllableException as ex:
                self._setStatus(Controllable.STATUS.Error)
                self._log.error("Exception at startup: %s", ex)

    @abstractmethod
    def _doStop(self):
        '''Stop the component's processing.  Should perform actual shutdown.
          Base class takes care of logging, messaging, and state change.
          Must return boolean indicating success of operation.
          Implementing classes should throw ControllableException on error.'''
        pass

    def stop(self):
        '''Perform actual stop, wraps call to _doStop.  This method takes care of setting the self._stop event.
        There is little benefit to overriding this method.'''
        if self._status == Controllable.STATUS.Started:
            self._setStatus(Controllable.STATUS.Stopping)
            try:
                self._log.debug("Stopping component [%s]...", self._name())
                self._stop.set()
                stat = self._doStop()
                if stat:
                    self._log.debug("Component [%s] stopped.", self._name())
                else:
                    self._log.warning("Unable to stop component [%s]", self._name())
                newStatus = Controllable.STATUS.Stopped if stat else Controllable.STATUS.Started
                self._setStatus(newStatus)
            except ControllableException as ex:
                self._setStatus(Controllable.STATUS.Error)
                self._log.error("Exception at stop: %s", ex)

    def getStatus(self):
        return self._status

    def _setStatus(self, status):
        if status <> self._status:
            self._status = status
            self._messenger.publish(TOPIC_COMPONENT_STATUS, status)
