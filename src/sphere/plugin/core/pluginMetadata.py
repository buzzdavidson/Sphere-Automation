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
from sphere.core.device import BaseSphereEntity

class PluginMetadata(BaseSphereEntity):
    def __init__(self):
        BaseSphereEntity.__init__(self)
        self._version = None
        self._url = None
        self._author = None
        self._depends = list()
        self._enabled = False
        self._installed = False
        self._lastUpdateDate = None

        # TODO add plugin categories (enum?)
        # plugin types:
        # - Bus provider: provides a device bus (?)
        # - Data Consumer: reads data from device data stream and does something with it (ie, RRD generation from sensors)
        # - Data Provider: feeds data into device data stream
        # - Widget - provides UI Widget
        # - Data Bridge: bridges between messaging technologies (ie, xPL bridge)

        # TODO add
        


