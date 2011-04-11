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
from sphere.common.enum import Enum

class EnumTests(unittest.TestCase):
    def setUp(self):
        self.enum = Enum('Dog','Cat','Fish')


    def testEmptyNotAllowed(self):
        try:
            enum = Enum()
        except AssertionError:
            pass
        else:
            fail("Expected assertion - empty enums not allowed")

    def testInclusion(self):
        assert self.enum.Cat

    def testInclusion_case(self):
        try:
            items = self.enum.cat
        except:
            pass
        else:
            fail("Expected assertion - enums are case sensitive")

    def testExclusion(self):
        try:
            items = self.enum.Frog
        except:
            pass
        else:
            fail("Expected assertion - item not in set")

    def testEquals(self):
        cat = self.enum.Cat
        anotherCat = self.enum.Cat

        assert (cat == anotherCat)

    def testLength(self):
        assert(self.enum.__len__() == 3)

if __name__ == '__main__':
    unittest.main()
