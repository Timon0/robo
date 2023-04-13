#!/usr/bin/env python
# Class autogenerated from .\alchestbuttonproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running





class ALChestButton(object):
    def __init__(self, session):
        self.session = session
        self.proxy = None

    def force_connect(self):
        self.proxy = self.session.service("ALChestButton")

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALChestButton")
        return self.proxy.ping()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALChestButton")
        return self.proxy.version()
