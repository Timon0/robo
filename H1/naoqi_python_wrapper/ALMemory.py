#!/usr/bin/env python
# Class autogenerated from .\almemoryproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running





class ALMemory(object):
    def __init__(self, session):
        self.session = session
        self.proxy = None

    def force_connect(self):
        self.proxy = self.session.service("ALMemory")

    def addMapping(self, service, signal, event):
        """Add a mapping between signal and event

        :param str service: Name of the service
        :param str signal: Name of the signal
        :param str event: Name of the event
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.addMapping(service, signal, event)

    def addMapping2(self, service, signalEvent):
        """Add a mapping between signal and event

        :param str service: Name of the service
        :param std::map<std::string, std::string> signalEvent: A map of signal corresponding to event
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.addMapping(service, signalEvent)

    def declareEvent(self, eventName):
        """Declares an event to allow future subscriptions to the event

        :param str eventName: The name of the event
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.declareEvent(eventName)

    def declareEvent2(self, eventName, extractorName):
        """Declares an event to allow future subscriptions to the event

        :param str eventName: The name of the event
        :param str extractorName: The name of the extractor capable of creating the event
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.declareEvent(eventName, extractorName)

    def getData(self, key):
        """Gets the value of a key-value pair stored in memory

        :param str key: Name of the value.
        :returns AL::ALValue: The data as an ALValue. This can often be cast transparently into the original type.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getData(key)

    def getData2(self, key, deprecatedParameter):
        """DEPRECATED - Gets the value of a key-value pair stored in memory. Please use the version of this method with no second parameter.

        :param str key: Name of the value.
        :param int deprecatedParameter: DEPRECATED - This parameter has no effect, but is left for compatibility reason.
        :returns AL::ALValue: The data as an ALValue
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getData(key, deprecatedParameter)

    def getDataList(self, filter):
        """Gets a list of all key names that contain a given string

        :param str filter: A string used as the search term
        :returns std::vector<std::string>: A list of all the data key names that contain the given string.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getDataList(filter)

    def getDataListName(self):
        """Gets the key names for all the key-value pairs in memory

        :returns std::vector<std::string>: A list containing the keys in memory
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getDataListName()

    def getDataOnChange(self, key, deprecatedParameter):
        """DEPRECATED - Blocks the caller until the value of a key changes

        :param str key: Name of the data.
        :param int deprecatedParameter: DEPRECATED - this parameter has no effect
        :returns AL::ALValue: an array containing all the retrieved data
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getDataOnChange(key, deprecatedParameter)

    def getDataPtr(self, key):
        """Gets a pointer to 32 a bit data item. Beware, the pointer will only be valid during the lifetime of the ALMemory object. Use with care, at initialization, not every loop. Insert a data item if needed. Throw if the data item has not the expected type. Only meaningful when called from code running in the same process as ALMemory.

        :param str key: Name of the data.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getDataPtr(key)

    def getIntPtr(self, key):
        """Gets a pointer to a int data item. Beware, the pointer will only be valid during the lifetime of the ALMemory object. Use with care, at initialization, not every loop. Insert a data item if needed. Throw if the data item has not the expected type. Only meaningful when called from code running in the same process as ALMemory.

        :param str key: Name of the data.
        :returns int: A pointer to int
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getIntPtr(key)

    def getFloatPtr(self, key):
        """Gets a pointer to a float data item. Beware, the pointer will only be valid during the lifetime of the ALMemory object. Use with care, at initialization, not every loop. Insert a data item if needed. Throw if the data item has not the expected type. Only meaningful when called from code running in the same process as ALMemory.

        :param str key: Name of the data.
        :returns float: A pointer to float
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getFloatPtr(key)

    def getDescriptionList(self, keylist):
        """Descriptions of all given keys

        :param std::vector<std::string> keylist: List of keys. (empty to get all descriptions)
        :returns AL::ALValue: an array of tuple (name, type, description) describing all keys.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getDescriptionList(keylist)

    def getEventHistory(self, key):
        """Get data value and timestamp

        :param str key: Name of the variable
        :returns AL::ALValue: A list of all the data key names that contain the given string.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getEventHistory(key)

    def getEventList(self):
        """Gets a list containing the names of all the declared events

        :returns std::vector<std::string>: A list containing the names of all events
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getEventList()

    def getExtractorEvent(self, extractorName):
        """Gets the list of all events generated by a given extractor

        :param str extractorName: The name of the extractor
        :returns std::vector<std::string>: A list containing the names of the events associated with the given extractor
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getExtractorEvent(extractorName)

    def getListData(self, keyList):
        """Gets the values associated with the given list of keys. This is more efficient than calling getData many times, especially over the network.

        :param AL::ALValue keyList: An array containing the key names.
        :returns AL::ALValue: An array containing all the values corresponding to the given keys.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getListData(keyList)

    def getMicroEventList(self):
        """Gets a list containing the names of all the declared micro events

        :returns std::vector<std::string>: A list containing the names of all the microEvents
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getMicroEventList()

    def getSubscribers(self, name):
        """Gets a list containing the names of subscribers to an event.

        :param str name: Name of the event or micro-event
        :returns std::vector<std::string>: List of subscriber names
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getSubscribers(name)

    def getTimestamp(self, key):
        """Get data value and timestamp

        :param str key: Name of the variable
        :returns AL::ALValue: A list of all the data key names that contain the given string.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getTimestamp(key)

    def getType(self, key):
        """Gets the storage class of the stored data. This is not the underlying POD type.

        :param str key: Name of the variable
        :returns str: String type: Data, Event, MicroEvent
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.getType(key)

    def insertData(self, key, value):
        """Inserts a key-value pair into memory, where value is a string

        :param str key: Name of the value to be inserted.
        :param str value: The string to be inserted
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.insertData(key, value)

    def insertData2(self, key, value):
        """Inserts a key-value pair into memory, where value is an int

        :param str key: Name of the value to be inserted.
        :param int value: The int to be inserted
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.insertData(key, value)

    def insertData3(self, key, value):
        """Inserts a key-value pair into memory, where value is a float

        :param str key: Name of the value to be inserted.
        :param float value: The float to be inserted
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.insertData(key, value)

    def insertData4(self, key, data):
        """Inserts a key-value pair into memory, where value is an ALValue

        :param str key: Name of the value to be inserted.
        :param AL::ALValue data: The ALValue to be inserted. This could contain a basic type, or a more complex array. See the ALValue documentation for more information.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.insertData(key, data)

    def insertListData(self, list):
        """Inserts a list of key-value pairs into memory.

        :param AL::ALValue list: An ALValue list of the form [[Key, Value],...]. Each item will be inserted.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.insertListData(list)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.ping()

    def raiseEvent(self, name, value):
        """Publishes the given data to all subscribers.

        :param str name: Name of the event to raise.
        :param AL::ALValue value: The data associated with the event. This could contain a basic type, or a more complex array. See the ALValue documentation for more information.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.raiseEvent(name, value)

    def raiseMicroEvent(self, name, value):
        """Publishes the given data to all subscribers.

        :param str name: Name of the event to raise.
        :param AL::ALValue value: The data associated with the event. This could contain a basic type, or a more complex array. See the ALValue documentation for more information.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.raiseMicroEvent(name, value)

    def removeData(self, key):
        """Removes a key-value pair from memory

        :param str key: Name of the data to be removed.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.removeData(key)

    def removeEvent(self, name):
        """Removes a event from memory and unsubscribes any exiting subscribers.

        :param str name: Name of the event to remove.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.removeEvent(name)

    def removeMicroEvent(self, name):
        """Removes a micro event from memory and unsubscribes any exiting subscribers.

        :param str name: Name of the event to remove.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.removeMicroEvent(name)

    def setDescription(self, name, description):
        """Describe a key

        :param str name: Name of the key.
        :param str description: The description of the event (text format).
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.setDescription(name, description)

    def subscribeToEvent(self, name, callbackModule, callbackMethod):
        """Subscribes to an event and automaticaly launches the module that declared itself as the generator of the event if required.

        :param str name: The name of the event to subscribe to
        :param str callbackModule: Name of the module to call with notifications
        :param str callbackMethod: Name of the module's method to call when a data is changed
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.subscribeToEvent(name, callbackModule, callbackMethod)

    def subscribeToEvent2(self, name, callbackModule, callbackMessage, callbacMethod):
        """DEPRECATED Subscribes to event and automaticaly launches the module capable of generating the event if it is not already running. Please use the version without the callbackMessage parameter.

        :param str name: The name of the event to subscribe to
        :param str callbackModule: Name of the module to call with notifications
        :param str callbackMessage: DEPRECATED Message included in the notification.
        :param str callbacMethod: Name of the module's method to call when a data is changed
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.subscribeToEvent(name, callbackModule, callbackMessage, callbacMethod)

    def subscribeToMicroEvent(self, name, callbackModule, callbackMessage, callbackMethod):
        """Subscribes to a microEvent. Subscribed modules are notified on theircallback method whenever the data is updated, even if the new value is the same as the old value.

        :param str name: Name of the data.
        :param str callbackModule: Name of the module to call with notifications
        :param str callbackMessage: Message included in the notification. This can be used to disambiguate multiple subscriptions.
        :param str callbackMethod: Name of the module's method to call when a data is changed
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.subscribeToMicroEvent(name, callbackModule, callbackMessage, callbackMethod)

    def subscriber(self, eventName):
        """Get an object wrapping a signal bound to the given ALMemory event. Create the event if it does not exist.

        :param str eventName: Name of the ALMemory event
        :returns qi::AnyObject: An AnyObject with a signal named "signal"
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.subscriber(eventName)

    def unregisterModuleReference(self, moduleName):
        """Informs ALMemory that a module doesn't exist anymore.

        :param str moduleName: Name of the departing module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.unregisterModuleReference(moduleName)

    def unsubscribeToEvent(self, name, callbackModule):
        """Unsubscribes a module from the given event. No further notifications will be received.

        :param str name: The name of the event
        :param str callbackModule: The name of the module that was given when subscribing.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.unsubscribeToEvent(name, callbackModule)

    def unsubscribeToMicroEvent(self, name, callbackModule):
        """Unsubscribes from the given event. No further notifications will be received.

        :param str name: Name of the event.
        :param str callbackModule: The name of the module that was given when subscribing.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.unsubscribeToMicroEvent(name, callbackModule)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALMemory")
        return self.proxy.version()
