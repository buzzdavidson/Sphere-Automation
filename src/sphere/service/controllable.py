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
from abc import ABCMeta, abstractmethod
import threading
from sphere.common.enum import Enum
from sphere.service.messenger.messenger import Messenger
from sphere.service.plumberjack import  messengerFactory, logFactory

class ControllableException(Exception):
    '''Exception for controllable instances'''
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)

class Controllable:
    '''ABC for controllable components (components with start/stop functionality)
    Adds basic features common to these components - lifecycle management,
    logging, and messenger.'''

    __metaclass__ = ABCMeta

    STATUS = Enum('Unknown','Starting','Started','Stopping','Stopped','Error')

    def __init__(self, name):
        self._name = name
        self._description = None
        self._status = Controllable.STATUS.Unknown
        self._messenger = messengerFactory.getMessenger(self)
        self._log = logFactory.getLogger(self)
        self._stop = threading.Event()

    name = property(lambda self: self._name)
    description = property(lambda self: self._description)
    status = property(lambda self: self._status)

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
                self._log.debug("Starting component [%s]...", self._name)
                self._stop.clear()
                stat = self._doStart()
                if stat:
                    self._log.debug("Component [%s] started.", self._name)
                else:
                    self._log.warning("Unable to start component [%s]!", self._name)
                # TODO: subscribe to messenger if started successfully
                newStatus = Controllable.STATUS.Started if stat else Controllable.STATUS.Stopped
                self._setStatus(newStatus)
            except Exception as ex:
                # TODO: should this exception be surfaced?
                self._setStatus(Controllable.STATUS.Error)
                self._log.error("Exception at startup: %s", ex)

    @abstractmethod
    def _doStop(self):
        '''Stop the component's processing.  Should perform actual shutdown.
          Base class takes care of logging, messaging, and state change.
          Must return boolean indicating success of operation.
          Implementing classes should throw ControllableException on error.'''
        pass

    @abstractmethod
    def _doRefresh(self):
        '''Perform component interval-based processing (if applicable)'''
        pass

    def stop(self):
        '''Perform actual stop, wraps call to _doStop.  This method takes care of setting the self._stop event.
        There is little benefit to overriding this method.'''
        if self._status == Controllable.STATUS.Started:
            self._setStatus(Controllable.STATUS.Stopping)
            try:
                self._log.debug("Stopping component [%s]...", self._name)
                self._stop.set()
                stat = self._doStop()
                if stat:
                    self._log.debug("Component [%s] stopped.", self._name)
                else:
                    self._log.warning("Unable to stop component [%s]", self._name)
                # TODO: unsubscribe all if stopped
                newStatus = Controllable.STATUS.Stopped if stat else Controllable.STATUS.Started
                self._setStatus(newStatus)
            except Exception as ex:
                # TODO: should this exception be surfaced?
                # TODO: this could leave background thread in inconsistent state
                self._setStatus(Controllable.STATUS.Error)
                self._log.error("Exception at stop: %s", ex)

    def refresh(self):
        if self._status == Controllable.STATUS.Started:
            self._log.debug("[%s] Executing refresh loop", self._name)
            self._doRefresh()

    def _setStatus(self, status):
        if status <> self._status:
            self._status = status
            self._messenger.publish(self, Messenger.TOPIC_COMPONENT_STATUS, status)

def startComponent(controllable):
    controllable.start()
    # TODO delay loop/ return once started


def stopComponent(controllable):
    controllable.stop()
    # TODO delay loop/ return once stopped

