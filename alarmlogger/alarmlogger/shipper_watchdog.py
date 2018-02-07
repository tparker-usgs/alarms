# -*- coding: utf8 -*-
"""
Ship messages to avosouth
"""
from datetime import datetime, timedelta
from io import StringIO
import logging
import os
import time

import paramiko
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent, FileCreatedEvent

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):
            self._ship(event.src_path)
        else:
            print("Skipping {}: {}".format(type(event), event.src_path))

    def on_modified(self, event):
        if isinstance(event, FileModifiedEvent):
            self._ship(event.src_path)
        else:
            print("Skipping {}: {}".format(type(event), event.src_path))
        
    def _ship(self, path):
            print("Found: {}".format(path))

    def on_hold(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().addHandler(logging.StreamHandler())
        logging.getLogger().setLevel(logging.DEBUG)

        transport = paramiko.Transport((os.environ['WEB_HOST']))
        pkey = paramiko.RSAKey.from_private_key(StringIO(os.environ['PRIVATE_KEY'].replace('\\n', '\n')))
        user = os.environ['USER']

        while True:
            transport.connect(pkey=pkey, username=user)
            sftp = paramiko.SFTPClient.from_transport(transport)
            remote_path = os.environ['WEB_PATH'] + os.environ['HOSTNAME']
            try:
                sftp.chdir(remote_path)
            except IOError:
                sftp.mkdir(remote_path)
                sftp.chdir(remote_path)

            filename_pattern = os.environ['HOSTNAME'] + '_%Y%m%d.html'
            filename = datetime.now().strftime(filename_pattern)
            sftp.put(filename, filename)
            sftp.close()
            transport.close()
            time.sleep(60)

def ship():
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
