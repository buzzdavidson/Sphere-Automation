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
from sphere.service.messenger.messenger import MessengerException
from sphere.service.messenger.simpleMessenger import SimpleMessenger
from sphere.service.plumberjack import messengerFactory

class SimpleMessengerTests(unittest.TestCase):
    def setUp(self):
        self.target = SimpleMessenger()
        self.TOPIC = 'a'
        self.TOPIC2 = 'b'
        self.MESSAGE = 'This is a test'

    def testRegisterTopic(self):
        self.target.registerTopic(self.TOPIC)
        self.assertTrue(self.TOPIC in self.target.getTopics())

    def testPublish_unknownTopic(self):
        try:
            self.target.publish(self, self.TOPIC2, self.MESSAGE)
            self.fail('expected exception')
        except MessengerException:
            pass # this is expected
        except Exception:
            self.fail('expected MessengerException')

    def testSubscribe_unknownTopic(self):
        try:
            receiver = mock.Mock()
            self.target.subscribe(receiver, self.TOPIC2)
            self.fail('expected exception')
        except MessengerException:
            pass # this is expected
        except Exception:
            self.fail('expected MessengerException')

    def testPublish_knownTopic(self):
        self.target.registerTopic(self.TOPIC)
        receiver = mock.Mock()
        receiver.messengerCallback = mock.Mock()
        self.target.subscribe(receiver, self.TOPIC)
        self.target.publish(self, self.TOPIC, self.MESSAGE)
        receiver.messengerCallback.assert_called_once_with(self.TOPIC, self.MESSAGE)

    def testPublish_knownTopic_multiRecipients(self):
        self.target.registerTopic(self.TOPIC)
        self.target.registerTopic(self.TOPIC2)
        receiver1 = mock.Mock()
        receiver1.messengerCallback = mock.Mock()
        receiver2 = mock.Mock()
        receiver2.messengerCallback = mock.Mock()
        receiver3 = mock.Mock()
        receiver3.messengerCallback = mock.Mock()
        self.target.subscribe(receiver1, self.TOPIC)
        self.target.subscribe(receiver2, self.TOPIC2)
        self.target.subscribe(receiver3, self.TOPIC)
        self.target.publish(self, self.TOPIC, self.MESSAGE)
        receiver1.messengerCallback.assert_called_once_with(self.TOPIC, self.MESSAGE)
        self.assertFalse(receiver2.messengerCallback.called)
        receiver3.messengerCallback.assert_called_once_with(self.TOPIC, self.MESSAGE)

    def testPublish_knownTopic_multiRecipients_senderNotIncluded(self):
        self.target.registerTopic(self.TOPIC)
        self.target.registerTopic(self.TOPIC2)
        receiver1 = mock.Mock()
        receiver1.messengerCallback = mock.Mock()
        receiver2 = mock.Mock()
        receiver2.messengerCallback = mock.Mock()
        receiver3 = mock.Mock()
        receiver3.messengerCallback = mock.Mock()
        self.target.subscribe(receiver1, self.TOPIC)
        self.target.subscribe(receiver2, self.TOPIC2)
        self.target.subscribe(receiver3, self.TOPIC)
        self.target.publish(receiver1, self.TOPIC, self.MESSAGE)
        self.assertFalse(receiver1.messengerCallback.called)
        self.assertFalse(receiver2.messengerCallback.called)
        receiver3.messengerCallback.assert_called_once_with(self.TOPIC, self.MESSAGE)

    def testSubscribe(self):
        self.target.registerTopic(self.TOPIC)
        self.target.registerTopic(self.TOPIC2)
        receiver1 = mock.Mock()
        self.target.subscribe(receiver1, self.TOPIC)
        self.target.subscribe(receiver1, self.TOPIC2)
        self.assertTrue(self.target.isSubscribed(self.TOPIC, receiver1))
        self.assertTrue(self.target.isSubscribed(self.TOPIC2, receiver1))

    def testUnsubscribe(self):
        self.target.registerTopic(self.TOPIC)
        self.target.registerTopic(self.TOPIC2)
        receiver1 = mock.Mock()
        self.target.subscribe(receiver1, self.TOPIC)
        self.target.subscribe(receiver1, self.TOPIC2)
        self.target.unsubscribe(receiver1, self.TOPIC)
        self.assertFalse(self.target.isSubscribed(self.TOPIC, receiver1))
        self.assertTrue(self.target.isSubscribed(self.TOPIC2, receiver1))

    def testRemoveSubscriber(self):
        self.target.registerTopic(self.TOPIC)
        self.target.registerTopic(self.TOPIC2)
        receiver1 = mock.Mock()
        self.target.subscribe(receiver1, self.TOPIC)
        self.target.subscribe(receiver1, self.TOPIC2)
        self.target.removeSubscriber(receiver1)
        self.assertFalse(self.target.isSubscribed(self.TOPIC, receiver1))
        self.assertFalse(self.target.isSubscribed(self.TOPIC2, receiver1))

    def testRemoveSubscriber_multi(self):
        self.target.registerTopic(self.TOPIC)
        self.target.registerTopic(self.TOPIC2)
        receiver1 = mock.Mock()
        receiver2 = mock.Mock()
        self.target.subscribe(receiver1, self.TOPIC)
        self.target.subscribe(receiver1, self.TOPIC2)
        self.target.subscribe(receiver2, self.TOPIC)
        self.target.subscribe(receiver2, self.TOPIC2)
        self.target.removeSubscriber(receiver1)
        self.assertFalse(self.target.isSubscribed(self.TOPIC, receiver1))
        self.assertFalse(self.target.isSubscribed(self.TOPIC2, receiver1))
        self.assertTrue(self.target.isSubscribed(self.TOPIC, receiver2))
        self.assertTrue(self.target.isSubscribed(self.TOPIC2, receiver2))

if __name__ == '__main__':
    unittest.main()
