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
from sphere.core.bus import BusType
from sphere.core.device import DeviceType
from sphere.plugin.core.plugin import Plugin
from sphere.plugin.core.serialListenerPlugin import SerialListenerPlugin
from sphere.service.messenger.messenger import MessagePacket, Messenger

class W800(SerialListenerPlugin):
    def __init__(self, name):
        SerialListenerPlugin.__init__(self, 'W800')
        self._description = 'Plugin to support WGL W800 X10 RF Receiver'
        self._version = '0.1.0'
        self._requirements.append('coreX10 >= 0.1.0')

        # TODO: configurable params: device (serial port), duplicate message threshold

        self._validateMessages = False
        self._checksumError = 0
        self._deviceMessageLength = 4
        self._deviceName = 'w800'
        self._duplicateMessageThreshold = 2
        self._serialParams = {
            'baudrate' : 4800,
            'bytesize': 8,
            'parity': 'N',
            'stopbits': 1,
        }
        self._translators = (X10BasicTranslator(), X10SecurityTranslator())
        self._deviceBus = 'X10'
        self._mydeviceid = '1234' # TODO: get device id from device manager (bus, address)

    def _registerDeviceMetadata(self):
        self._deviceManager.registerDeviceType(DeviceType(deviceCategory='Interface', name='W800RF', description='W800 X10 RF Receiver', busType='X10'))

    def _loadConfiguration(self, configManager):
        self._device = '/dev/keyspan-0' # TODO: load device from config manager

    def _deviceCallback(self, message):
        # See WGL documentation (http://www.wgldesigns.com/protocols/w800rf32_protocol.txt)
        if len(message) <> self._deviceMessageLength:
            self._log.error("Expected %d bytes, received %d.  Ignoring message.  Message bytes follow: [%s]" % (self._deviceMessageLength, len(message), str(message).encode("hex")))
            return None

        # loop through translators, call translate on any that apply and fire notification if data returned
        translated = messaged = False
        for translator in self._translators:
            if translator.canTranslate(message):
                data = translator.translate(message)
                translated = True
                if data:
                    self._notify(Messenger.buildPacket(msgbus=self._deviceBus, msgdevice=self._mydeviceid, msgdata=data))
                    messaged = True

        if not translated:
            self._log.warning('No translator found to handle message [%s]', (str(message).encode("hex")))
        elif not messaged:
            self._log.debug('Message [%s] translated but generated no data', (str(message).encode("hex")))

class W800BaseTranslator:
    def _swapMessageBytes(self, message):
        r = list()
        for b in message:
            lob = b & 0x0f
            hob = b >> 4 & 0x0f
            swap = lob << 4 | hob
            r.append(swap)
        return tuple(r)

    def canTranslate(self, message):
        raise "Must be overridden in implementing class"
    def translate(self, message):
        raise  "Must be overridden in implementing class"

class X10BasicTranslator(W800BaseTranslator):
    # These are codes returned via my X10 Pro model PMS-03 indoor/outdoor wireless occupancy sensor.
    _HouseCodes = {
        0x06: 'A', 0x07: 'B', 0x04: 'C', 0x05: 'D', 0x08: 'E', 0x09: 'F', 0x0a: 'G', 0x0b: 'H',
        0x0e: 'I', 0x0f: 'J', 0x0c: 'K', 0x0d: 'L', 0x00: 'M', 0x01: 'N', 0x02: 'O', 0x03: 'P'
    }
    _DeviceCodes = {
        0x00: 1, 0x10: 2, 0x08: 3, 0x18: 4, 0x40: 5, 0x50: 6, 0x48: 7, 0x58: 8
    }
    _CommandCodes = {
        0x00: 'ON', 0x20: 'OFF', 0x80: 'ALL_OFF', 0x88: 'BRIGHT', 0x90: 'ALL_ON', 0x98: 'DIM'
    }

    def canTranslate(self, message):
        return (message[0] ^ 0xff == message[1]) and (message[2] ^ 0xff == message[3])

    def translate(self, message):
        data = message # dont swap bytes for these
        device = house = command = None
        bitmask = 0x98
        if not data[2] & 0x80:
            key = data[2] & 0x58
            if self._DeviceCodes.has_key(key):
                device = self._DeviceCodes[key]
                if data[0] & 0x04:
                    device += 8
            bitmask = 0x20

        key = (data[0] & 0xf0) >> 4
        house = self._HouseCodes[key] if self._HouseCodes.has_key(key) else 'M'
        key = data[2] & bitmask
        command = self._CommandCodes[key] if self._CommandCodes.has_key(key) else None
        return {'house' : house, 'device' : device, 'command' : command}

class X10SecurityTranslator(W800BaseTranslator):
    def canTranslate(self, message):
        return (message[0] ^ 0x0f == message[1]) and (message[2] ^ 0xff == message[3])

    def translate(self, message):
        msg = self._swapMessageBytes(message)
        data = msg[2]
        command = tamper = delay = lowbattery = alert = None
        alert = not bool(data & 0x01 or data &0x08) # PMS03 reports alert at bit 4
        tamper = bool(data & 0x02)
        delay = data & 0x20
        lowbattery = bool(data & 0x80)
        device = msg[0]
        return { 'device' : device, 'command' : command, 'alert' : alert, 
                 'tamper' : tamper, 'delay' : delay, 'lowbattery' : lowbattery }
