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

class Site(BaseSphereEntity):
    def __init__(self):
        BaseSphereEntity.__init__(self)
        self._buildings = list()

    buildings = property(lambda self: self._buildings)

    def addBuilding(self, building):
        self._buildings.append(building)

    def removeBuilding(self, building):
        self._buildings.remove(building)

class Building(CoreEntity):
    def __init__(self):
        BaseSphereEntity.__init__(self)
        self._floors = list()

    floors = property(lambda self: self._floors)

    def addFloor(self, floor):
        self._floors.append(floor)

    def removeBuilding(self, floor):
        self._floors.remove(floor)

class Floor(BaseSphereEntity):
    def __init__(self):
        BaseSphereEntity.__init__(self)
        self._rooms = list()

    rooms = property(lambda self: self._rooms)

    def addRoom(self, room):
        self._rooms.append(room)

    def removeRoom(self, room):
        self._rooms.remove(room)

class Room(BaseSphereEntity):
    def __init__(self):
        BaseSphereEntity.__init__(self)

class Vehicle(BaseSphereEntity):
    def __init__(self):
        BaseSphereEntity.__init__(self)
