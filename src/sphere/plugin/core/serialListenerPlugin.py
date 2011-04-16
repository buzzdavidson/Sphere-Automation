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
from time import time
from sphere.plugin.core.serialBasePlugin import SerialBasePlugin, SerialPluginException, BasicSerialHandler

class SerialListenerPlugin(SerialBasePlugin):
    '''Starting point for serial plugins which simply listen to messages coming from an underlying serial device.
    Provides a mechanism for the automatic removal of duplicate messages occurring within a specified timeframe.'''
    def __init__(self, name):
        SerialBasePlugin.__init__(self, name)
        self._duplicateMessageThreshold = 5

    def _getHandler(self, serialPort):
        return DedupeSerialHandler(self._serialPort, self._log, self._deviceCallback, self._messageLength, self._duplicateMessageThreshold)

class DedupeSerialHandler(BasicSerialHandler):
    def __init__(self, serialPort, log, messageCallback, messageLength, duplicateThreshold):
       BasicSerialHandler.__init__(self, serialPort, log, messageCallback, messageLength)
       self._dedupe = dict()
       self._duplicateMessageThreshold = duplicateThreshold

    def _messageHook(self, message):
        if self._duplicateMessageThreshold is not None:
            key = str(message).encode('hex')
            # TODO: max message length: how many bytes to define duplicate?
            # TODO: data aging - purge old data
            if self._dedupe.has_key(key):
                last = self._dedupe[key]
                delta = time.time() - last
                if delta < self._duplicateMessageThreshold:
                    self._log.debug('Discarding duplicate message (%s, age=%4.2f)' % (key, delta))
                    return None
            self._dedupe[key] = time.time()
        return message
