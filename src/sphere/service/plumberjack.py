#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
plumberjack provides a central mechanism for defining and configuring common components, such as logging.  It can
be thought of as a (very) simple IoC mechanism for the Sphere project.

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
import logging

class LogFactory():
    DEFAULT_LOGGER = 'Sphere'
    def __init__(self):
        # TODO initialize logger
        pass

    def getLogger(self, caller):
        if caller is None:
            return logging.getLogger(LogFactory.DEFAULT_LOGGER)
        if isinstance(caller, str):
            return logging.getLogger(caller)
        return logging.getLogger(type(caller))

class MessengerFactory():
    def __init__(self):
        # TODO initialize messenger
        pass

    def getMessenger(self, caller):
        # TODO: implement getMessenger
        # Method creates appropriate messenger instance and subscribes to default topics automatically
        return None


