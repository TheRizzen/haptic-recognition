#!/usr/bin/env python3

import sys
import socket
import json

ADDR = '192.168.33.2'
PORT = 53451

def cisors_check(fingers):
    if fingers[3]['ang'][0] >= 2 \
       and fingers[4]['ang'][0] >= 2 \
       and fingers[1]['ang'][0] <= 1.5 \
       and fingers[2]['ang'][0] <= 1.5 \
       and fingers[1]['ang'][1] <= 0.2 \
       and fingers[2]['ang'][1] >= 0:
        return True
    else:
        return False

def rock_check(fingers):
    if fingers[1]['ang'][0] >= 2 \
       and fingers[2]['ang'][0] >= 2 \
       and fingers[3]['ang'][0] >= 2 \
       and fingers[4]['ang'][0] >= 2:
        return True
    else:
        return False

def paper_check(fingers):
    if fingers[1]['ang'][0] <= 0 \
       and fingers[2]['ang'][0] <= 0.1 \
       and fingers[3]['ang'][0] <= 0.1 \
       and fingers[4]['ang'][0] <= 0.1:
        return True
    else:
        return False

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ADDR, PORT))
except ConnectionRefusedError:
    sys.exit(1)

while 1:
    data = s.recv(1024)
    data = data.decode().rstrip()
    try:
        pdata = json.loads(data)
    except json.decoder.JSONDecodeError:
        pass

    try:
        print(pdata['data']['fingers'][1])
        print(pdata['data']['fingers'][2])
        print(pdata['data']['fingers'][3])
        print(pdata['data']['fingers'][4])
        fingers = pdata['data']['fingers'];
        if cisors_check(fingers):
            print('CISORS')
        elif rock_check(fingers):
            print('ROCK')
        elif paper_check(fingers):
            print('PAPER')
        else:
            print('NOTHING')
    except KeyError:
        pass
s.close()

#s.send('{"dst": "cc:78:ab:ad:ac:0d","type": "vibration","data": {"type": "middle","dur": 65531, "str": 10}}\n'.encode('utf-8'));
