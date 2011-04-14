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
import threading
from time import time
from sphere.plugin.core.plugin import Plugin, PluginException

class SerialPluginException(PluginException):
    def __init__(self, value):
        PluginException.__init__(self, value)
        self.value = value

    def __str__(self):
        return repr(self.value)

class SerialBasePlugin(Plugin):
    '''Starting point for plugins which communicate with a serial port (or a device on a USB/Serial adapter).
    Interaction with serial port occurs on a managed background thread and received messages are passed back to
    plugin via a callback method.  Background thread lifecycle is managed by base class(es).'''
    def __init__(self, name, device=None):
        Plugin.__init__(self, name)
        self._device = device
        self._serialPort = None
        self._serialParams = {
            'port' : self._device,
            'baudrate' : 9600,
            'bytesize': 8,
            'parity': 'N',
            'stopbits': 1,
            'timeout': None
        }
        self._childThread = None
        self._serialHandler = None
        self._messageLength = None # set to number of bytes to have core component handle packet management, none to perform management yourself

    def initializePlugin(self, configManager, deviceManager):
        Plugin.initializePlugin(self, configManager, deviceManager)

    def _open(self):
        rv = False
        self._log.info("Try to open %s device using [%s]" % (self._name, self._serialParams))
        try:
            # see http://pyserial.sourceforge.net/pyserial_api.html#serial.serial_for_url
            sp = self._serialParams
            self._serialPort = serial.Serial(self._device, baudrate=sp['baudrate'], bytesize=sp['bytesize'],
                                              parity=sp['parity'], stopbits=sp['stopbits'], timeout=sp['timeout'])
            if self._serialPort.isOpen():
                self._log.info("%s device successfully opened." % self._name)
                rv = True
        except Exception as ex:
            msg = 'Exception opening serial device [%s]: %s' % (self._device, ex)
            self._log.error(msg)
            raise SerialPluginException(ex)
        return rv

    def _close(self):
        rv = False
        if self._serialPort is not None and self._serialPort.isOpen():
            try:
                self._serialPort.close()
                time.sleep(0.25)
                rv = not self._serialPort.isOpen()
                self._serialPort = None
            except Exception as ex:
                msg = 'Exception closing serial device [%s]: %s' % (self._device, ex)
                self._log.error(msg)
                raise SerialPluginException(ex)
        return rv

    def _startListening(self):
        self._log.info('Begin %s listen' % self._name)
        self._serialHandler = self._getHandler(self._serialPort)
        self._childThread = threading.Thread(None,
                                   self._serialHandler.listen,
                                   self._name + '_reader',
                                   (self._stop,),
                                   {})

    def _stopListening(self):
        # TODO: stop has already been set by controllable - is there anything to do here?  Wait for thread to exit?
        pass

    def _doStart(self):
        if self._open():
            self._startListening()
            return True
        return False

    def _doStop(self):
        self._stopListening()
        return self._close()

    def _getHandler(self, serialPort):
        return BasicSerialHandler(self._serialPort, self._log, self._deviceCallback, self._messageLength)

    def _deviceCallback(self, message):
        pass


class BasicSerialHandler:
    '''Simple serial port handler implementation, listens for data and passes received data back via callback method.
    Messages will be chunked into the size specified by messageLength parameter.  As this process occurs on a background
    thread, it is OK for it to block on read.'''
    def __init__(self, serialPort, log, messageCallback, messageLength):
        self._serialPort = serialPort
        self._log = log
        self._messageCallback = messageCallback
        self._messageLength = messageLength

    def listen(self, stop):
        try:
            while not stop.isSet():
                message = self._readFromDevice()
                if message is not None:
                    self._log.debug('Got %d bytes from device: %s', len(message), str(message).encode('hex'))
                    self._messageCallback(message)
            else:
                self._log.debug('Serial handler thread is stopping.')
        except Exception as ex:
            raise SerialPluginException(ex)


    def _readFromDevice(self):
        message = bytearray('')
        try:
            b = self._serialPort.read()
            while b is not None:
                if b is not None and len(b) > 0:
                    message.append(b)
                if self._serialPort.inWaiting():
                    b = self._serialPort.read()
                else:
                    break
                if b is not None and (self._messageLength is not None and len(b) == self._messageLength):
                    break
        except Exception as ex:
            raise SerialPluginException(ex)

        if message is not None and len(message) < 1:
            message = None

        return message
