#!/usr/bin/env python

import pika
import json
#import base64
import sqlite3
import os
from .db import Db

def main():
    user = os.environ['AVOBROKER_USER']
    passwd = os.environ['AVOBROKER_PASS']
    host = os.environ['AVOBROKER_HOST']
    mycred=pika.credentials.PlainCredentials(user, passwd)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=mycred))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                 exchange_type='fanout')

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs',
               queue=queue_name)

    db_conn = Db('/alarms')
    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        data = json.loads(body)
#        with open("image.jpg","wb") as fout:
#            fout.write(base64.b64decode(data['file']))

        print("New alarm:");
        print("volcano: {}".format(data['volcano']))
        print("subject: {}".format(data['subject']))
        print("message: {}".format(data['message']))
        print("\n\n");
        db_conn.insert_alarm(data)
        print("Alarm count: {}".format(db_conn.count_alarms()))

    conn = Db('/alarms')

    channel.basic_consume(callback,
                  queue=queue_name,
                  no_ack=True)

    channel.start_consuming()

if __name__=='__main__':
    main()
