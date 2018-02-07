# -*- coding: utf8 -*-
"""
Receive messages from broker, write to a file, and deliver to avosouth.
"""

from multiprocessing import Process, Queue

from .listener import Listener
from .shipper import ship

q = Queue()

# start listener
listener = Listener(q)
p = Process(target=listener.listen)
p.start()

# start file mover
p = Process(target=ship, args=(q,))
p.start()
