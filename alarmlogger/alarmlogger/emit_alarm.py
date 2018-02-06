#!/usr/bin/env python

from alarm_pb2 import Alarm
import pika
import sys
import base64
import json
from datetime import datetime, timedelta
from time import gmtime, strftime

mycred=pika.credentials.PlainCredentials('ewprocessing', 'avo..avo')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='avobroker1', credentials=mycred))
channel = connection.channel()
channel.exchange_declare(exchange='alarms',
                         exchange_type='topic')

#with open("rabbit-logo_dfefmx.jpg", "rb") as image_file:
    #encoded_string = base64.b64encode(image_file.read())
encoded_string="test"

alarm = Alarm()
alarm.name = "Tomp test alarm"
alarm.type = "TompAirwave"
alarm.state = Alarm.OK
alarm.region = "none"
alarm.message = "Test message\nline2\nline3"

routing_key="TomAirwave.MtTesting.triggered"
channel.basic_publish(exchange='alarms',
                      routing_key=routing_key,
                      body=alarm.SerializeToString())
print(" [x] Sent %r" % alarm)
connection.close()
