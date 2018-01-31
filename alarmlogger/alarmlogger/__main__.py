#!/usr/bin/env python

import pika
import os
from .broker import callback

user = os.environ['AVOBROKER_USER']
passwd = os.environ['AVOBROKER_PASS']
mycred=pika.credentials.PlainCredentials(user, passwd)

host = os.environ['AVOBROKER_HOST']
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=mycred))

channel = connection.channel()

exchange = os.environ['AVOBROKER_EXCHANGE']
channel.exchange_declare(exchange=exchange,
             exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=exchange,
           queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


channel.basic_consume(callback,
              queue=queue_name,
              no_ack=True)

channel.start_consuming()
