# -*- coding: utf8 -*-
"""
Receive messages from broker, write to a file, and deliver to avosouth.
"""

from multiprocessing import Process

from .listener import listen
from .shipper import ship

# start listener
p = Process(target=listen)
p.start()

# start file mover
p = Process(target=ship)
p.start()
