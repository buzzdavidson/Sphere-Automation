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
from sphere.service.messenger.messenger import Messenger, MessengerException
from sphere.service.plumberjack import logFactory

class SimpleMessenger(Messenger):
    '''Trivial implementation of messenger FOR DEVELOPMENT PURPOSES ONLY.'''
    def __init__(self):
        self._topics=dict()
        self._log = logFactory.getLogger('SimpleMessenger')

    def publish(self, sender, topic, message):
        if not self._topics.has_key(topic):
            raise MessengerException('Unknown topic ' + topic, topic)
        self._log.debug('Publishing message [%s] to topic [%s]', message, topic)
        for tpl in self._topics[topic]:
            if tpl <> sender:
                self._log.debug('Publishing message to recipient [%s]', str(tpl))
                tpl.messengerCallback(topic, message)

    def subscribe(self, subscriber, topic, callback=None):
        if not self._topics.has_key(topic):
            raise MessengerException('Unknown topic ' + topic, topic)
        cb = callback
        if cb is None:
            if subscriber.messengerCallback is None:
                raise MessengerException(str('Class [%s] contains no messengerCallback method and callback not specified in subscribe call' % type(subscriber)))
            else:
                cb = subscriber.messengerCallback

        if self.isSubscribed(topic, subscriber, cb):
            self._log.debug('Component [%s] is already subscribed to topic [%s]', str(subscriber), topic)
        else:
            self._log.debug('Subscribing component [%s] to topic [%s]', str(subscriber), topic)
            self._topics[topic].append(subscriber)

    def isSubscribed(self, topic, subscriber, callback=None):
        for tpl in self._topics[topic]:
            if tpl == subscriber:
                return True
        return False

    def registerTopic(self, topic):
        self._log.debug('Registering topic [%s]', topic)
        self._topics[topic] = list()

    def getTopics(self):
        return self._topics.keys()

    def unsubscribe(self, subscriber, topic):
        remove = None
        for tpl in self._topics[topic]:
            if tpl == subscriber:
                remove = tpl
                break
        if remove is not None:
            self._log.debug('Unsubscribing %s from topic [%s]', str(subscriber), topic)
            self._topics[topic].remove(remove)

    def removeSubscriber(self, subscriber):
        self._log.debug('Removing subscriber %s from all topics', str(subscriber))
        for topic in self._topics.keys():
            self.unsubscribe(subscriber, topic)

