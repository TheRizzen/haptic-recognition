#!/usr/bin/env python3

import sys
import socket
import json

ADDR = '192.168.33.2'
PORT = 53451

def send_vibration(finger_str):
    payload = '{"dst": "cc:78:ab:ad:ac:0d","type": "vibration","data": {"type": "%s","dur": 655, "str": 10}}\n' % finger_str
    payload = payload.encode('utf-8')
    s.send(payload);

def send_vibration_all():
    send_vibration('index')
    send_vibration('middle')
    send_vibration('third')
    send_vibration('little')

def print_fingers(fingers):
    print(fingers[1])
    print(fingers[2])
    print(fingers[3])
    print(fingers[4])

def cisors_check(fingers):
    if fingers[3]['ang'][0] >= 2 \
       and fingers[4]['ang'][0] >= 2 \
       and fingers[1]['ang'][0] <= 0.3 \
       and fingers[2]['ang'][0] <= 0.3 \
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

def detect_sign(fingers):
    if cisors_check(fingers):
        return 'CISORS'
    elif rock_check(fingers):
        return 'ROCK'
    elif paper_check(fingers):
        return 'PAPER'
    else:
        return 'NOTHING'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ADDR, PORT))
except ConnectionRefusedError:
    sys.exit(1)

sign = 'NOTHING'
while 1:
    data = s.recv(1024)
    data = data.decode().rstrip()
    try:
        pdata = json.loads(data)
    except json.decoder.JSONDecodeError:
        pass

    try:
        fingers = pdata['data']['fingers'];
        print_fingers(fingers)
        old_sign = sign;
        sign = detect_sign(fingers)
        if old_sign != sign and sign != 'NOTHING':
            send_vibration_all()
        print(sign)
    except KeyError:
        pass
s.close()

