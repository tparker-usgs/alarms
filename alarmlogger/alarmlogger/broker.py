# -*- coding: utf8 -*-
"""
Receive messages from broker.
"""
import json

from .alarm_pb2 import Alarm

FILENAME_SUFFIX = "_%Y%m%d.pb2"

def callback(ch, method, properties, body):
    print("ROUTING KEY", method.routing_key)
    alarm = Alarm()
    #alarm.ParseFromString(body)

    now = datetime.now()
    suffix = now.strftime(FILENAME_SUFFIX)

    short_name = filter(str.isalnum, alarm.name)
    filename = "{}.{}.{}.{}".format(alarm.type, alarm.name, alarm.state)
    #with open(filename, 'ab') as f:
    #    f.write(alarm.SerializeToString())

