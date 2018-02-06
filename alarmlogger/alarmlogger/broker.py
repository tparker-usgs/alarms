# -*- coding: utf8 -*-
"""
Receive messages from broker.
"""
import json

import alarm_pb2

FILENAME_SUFFIX = "_%Y%m%d.pb2"

def callback(ch, method, properties, body):
    print("ROUTING KEY", method.routing_key)
    alarm = alarm_pb2.Alarm()
    alarm.ParseFromString(body)

    now = datetime.now()
    suffix = now.strftime(FILENAME_SUFFIX)

    short_name = filter(str.isalnum, alarm.name)
    filename = "{}.{}.{}.{}".format(alarm.type, alarm.name, alarm.state)
    with open(this_file, 'ab') as f:
        f.write(alarm.SerializeToString())


def print_message(alarm):
    print("New alarm:");
    print("volcano: {}".format(alarm['volcano']))
    print("subject: {}".format(alarm['subject']))
    print("message: {}".format(alarm['message']))
    print("\n\n");
