# -*- coding: utf8 -*-
"""
Receive messages from broker.
"""
from .alarm_pb2 import Alarm
from datetime import datetime
import json
import re

FILENAME_SUFFIX = "%Y%m%d.pb2"

def callback(ch, method, properties, body):
    print("ROUTING KEY", method.routing_key)
    alarm = Alarm()
    alarm.ParseFromString(body)

    now = datetime.now()
    suffix = now.strftime(FILENAME_SUFFIX)

    short_name = re.sub("[^a-zA-Z0-9]", "", alarm.name)
    state_name = Alarm.State.Name(alarm.state)
    filename = "{}.{}.{}_{}".format(alarm.type, short_name, state_name, suffix)
    with open(filename, 'ab') as f:
        f.write(alarm.SerializeToString())

