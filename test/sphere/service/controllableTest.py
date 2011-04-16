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

import unittest
from sphere.service.controllable import Controllable
import mock
from mock import patch
from sphere.service.plumberjack import messengerFactory

class SampleControllable(Controllable):
    def __init__(self, name='sample'):
        Controllable.__init__(self, name)
        self.startReturn = True
        self.stopReturn = True

    def _doStart(self):
        return self.startReturn

    def _doStop(self):
        return self.stopReturn

    def _doRefresh(self):
        pass

class ControllableTests(unittest.TestCase):
    def setUp(self):
        self.mockMessenger = mock.Mock()
        messengerFactory.getMessenger = mock.Mock()
        messengerFactory.getMessenger.return_value = self.mockMessenger
        self.target = SampleControllable()

    def test_start_started(self):
        self.target.start()
        assert(self.target.status == SampleControllable.STATUS.Started)
        
    def test_start_canstart_from_error(self):
        self.target._status = SampleControllable.STATUS.Error
        self.target.start()
        assert(self.target.status == SampleControllable.STATUS.Started)

    def test_start_canstart_from_stopped(self):
        self.target._status = SampleControllable.STATUS.Stopped
        self.target.start()
        assert(self.target.status == SampleControllable.STATUS.Started)

    def test_start_canstart_from_unknown(self):
        self.target._status = SampleControllable.STATUS.Unknown
        self.target.start()
        assert(self.target.status == SampleControllable.STATUS.Started)

    def test_start_exception(self):
        self.target._doStart = mock.Mock()
        self.target._doStart.side_effect = Exception('Boom!')
        self.target._status = SampleControllable.STATUS.Unknown
        self.target.start()
        assert(self.target.status == SampleControllable.STATUS.Error)

    def test_stop_stopped(self):
        self.target._status = SampleControllable.STATUS.Started
        self.target.stop()
        assert(self.target.status == SampleControllable.STATUS.Stopped)
        
    def test_stop_cantstop_from_error(self):
        self.target._status = SampleControllable.STATUS.Error
        self.target.stop()
        assert(self.target.status == SampleControllable.STATUS.Error)

    def test_stop_exception(self):
        self.target._status = SampleControllable.STATUS.Started
        self.target._doStop = mock.Mock()
        self.target._doStop.side_effect = Exception('Boom!')
        self.target.stop()
        assert(self.target.status == SampleControllable.STATUS.Error)

if __name__ == '__main__':
    unittest.main()
