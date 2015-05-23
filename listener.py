import os.path

import bcolz
import numpy as np
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

if not os.path.exists('db'):
    print("db not found, creating")
    ct = bcolz.ctable([np.empty(0, dtype="i8")],
                      names=['data'],
                      rootdir='db',
                      )
else:
    print("db found, initializing")
    ct = bcolz.open('db')

while True:
    message = socket.recv()
    print("Received request: %s" % message)
    ct.append((message,))
    ct.flush()
    socket.send(b"OK")
