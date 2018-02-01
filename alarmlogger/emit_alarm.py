#!/usr/bin/env python

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

t2_local = datetime.now()
t1_local = t2_local + timedelta(hours=-1)
t2 = datetime.utcnow()
t1 = t2 + timedelta(hours=-1)

message='TompAirwave alarm:\n'
message+='Mt. Testing detection!\n\n'
message+='Start: {} (UTC)\nEnd: {} (UTC)\n\n'.format(t1.strftime('%Y-%m-%d %H:%M'),t2.strftime('%Y-%m-%d %H:%M'))
message+='Start: {} ({})'.format(t1_local.strftime('%Y-%m-%d %H:%M'),t1_local.tzname())
message+='\nEnd: {} ({})\n\n'.format(t2_local.strftime('%Y-%m-%d %H:%M'),t2_local.tzname())
message+='d_Azimuth: 90 degrees\n'
message+='Velocity: 5 m/s\n'
message+='Max Pressure: 2 Pa'

data = {
    "volcano": "Mt. Testing",
    "subject": "Mt. Testing Airwave Detection",
    "message": message
}
routing_key="TomAirwave.MtTesting.triggered"
channel.basic_publish(exchange='alarms',
                      routing_key=routing_key,
                      body=json.dumps(data))
print(" [x] Sent %r" % message)
connection.close()
