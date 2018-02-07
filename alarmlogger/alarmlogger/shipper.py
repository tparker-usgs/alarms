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

def ship(queue):
    while True:
        print("Found {}".format(queue.get()))
