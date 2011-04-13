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
from sphere.core.actuator import ActuatorType
from sphere.core.device import DeviceType
from sphere.core.sensor import SensorType
from sphere.plugin.core.plugin import Plugin

class CoreDevices(Plugin):
    def __init__(self):
        Plugin.__init__(self, 'CoreDevices')
        self._description = 'Core Device Plugin'

    def _doStart(self):
        return True

    def _doStop(self):
        return True

    def _registerDeviceMetadata(self):
        self._deviceRegistry.registerDeviceCategory('Sensor')
        self._deviceRegistry.registerDeviceCategory('Actuator')
        self._deviceRegistry.registerDeviceCategory('Light')
        self._deviceRegistry.registerDeviceCategory('Appliance')
        self._deviceRegistry.registerDeviceType(SensorType(name='Thermometer', description='Temperature Sensor', dataType=DeviceType.DATA_TYPES.Float))
        self._deviceRegistry.registerDeviceType(SensorType(name='Barometer', description='Barometric Pressure Sensor', dataType=DeviceType.DATA_TYPES.Float))
        self._deviceRegistry.registerDeviceType(SensorType(name='Hygrostat', description='Humidity Sensor', dataType=DeviceType.DATA_TYPES.Float))
        self._deviceRegistry.registerDeviceType(SensorType(name='Photometer', description='Light Sensor', dataType=DeviceType.DATA_TYPES.Float))
        self._deviceRegistry.registerDeviceType(SensorType(name='Voltmeter', description='Voltage Sensor', dataType=DeviceType.DATA_TYPES.Float))
        self._deviceRegistry.registerDeviceType(SensorType(name='Ammeter', description='Current Sensor', dataType=DeviceType.DATA_TYPES.Float))
        self._deviceRegistry.registerDeviceType(SensorType(name='Counter', description='Counter', dataType=DeviceType.DATA_TYPES.Integer))
        self._deviceRegistry.registerDeviceType(SensorType(name='Digital', description='General ON/OFF Sensor', dataType=DeviceType.DATA_TYPES.Boolean))
        self._deviceRegistry.registerDeviceType(SensorType(name='Analog', description='General Analog Sensor', dataType=DeviceType.DATA_TYPES.Float))
        # TODO: pressure sensor
        # TODO: gas sensor, Flow sensor
        # TODO: does it make sense to add subcategories (ie sensor/environmental?)
        # TODO: security devices: motion detector, breakage detector
        # TODO: weather devices (barometer probably belongs here): rain meter, wind speed, wind direction, UV meter, gas sensor, moisture detector, etc
        self._deviceRegistry.registerDeviceType(ActuatorType(name='Switch', description='Basic ON/OFF Switch', dataType=DeviceType.DATA_TYPES.Boolean))
        self._deviceRegistry.registerDeviceType(ActuatorType(name='Relay', description='Remotely Controlled Switch',dataType=DeviceType.DATA_TYPES.Boolean))
        # TODO: define allowed states for dimmer
        self._deviceRegistry.registerDeviceType(ActuatorType(name='Dimmer', description='Analog Actuator',dataType=DeviceType.DATA_TYPES.Float))
        # TODO: HVAC: heat, cool, fan, damper, humidifier, thermostat