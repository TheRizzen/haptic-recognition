#!/usr/bin/env python3

import sys
import socket
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host')
parser.add_argument('port', type=int)
args = parser.parse_args()

def read_json_payload(s):
    data = s.recv(1024)
    data = data.decode().rstrip()
    try:
        pdata = json.loads(data)
        return pdata
    except json.decoder.JSONDecodeError:
        pass

# Send vibration to a finger
def send_vibration(dst, finger_str):
    payload = '{"dst": "%s","type": "vibration","data": {"type": "%s","dur": 655, "str": 10}}\n' % (dst, finger_str)
    payload = payload.encode('utf-8')
    s.send(payload);

# Send vibration to all fingers
def send_vibration_all(dst):
    send_vibration(dst, 'index')
    send_vibration(dst, 'middle')
    send_vibration(dst, 'third')
    send_vibration(dst, 'little')

# Print fingers data
def print_fingers(fingers):
    print(fingers[1])
    print(fingers[2])
    print(fingers[3])
    print(fingers[4])

# Compare the fingers position with the position of a sign
def cisors_check(fingers):
    if fingers[3]['ang'][0] >= 2 \
       and fingers[4]['ang'][0] >= 2 \
       and fingers[1]['ang'][0] <= 0.5 \
       and fingers[2]['ang'][0] <= 0.5 \
       and fingers[1]['ang'][1] <= 0.2 \
       and fingers[2]['ang'][1] >= 0:
        return True
    else:
        return False

# Compare the fingers position with the position of a sign
def rock_check(fingers):
    if fingers[1]['ang'][0] >= 2 \
       and fingers[2]['ang'][0] >= 2 \
       and fingers[3]['ang'][0] >= 2 \
       and fingers[4]['ang'][0] >= 2:
        return True
    else:
        return False

# Compare the fingers position with the position of a sign
def ninja_check(fingers):
    if fingers[1]['ang'][0] <= 0.5 \
       and fingers[2]['ang'][0] <= 0.5 \
       and fingers[3]['ang'][0] >= 2 \
       and fingers[4]['ang'][0] >= 2:
        return True
    else:
        return False

# Compare the fingers position with the position of a sign
def paper_check(fingers):
    if fingers[1]['ang'][0] <= 0 \
       and fingers[2]['ang'][0] <= 0.1 \
       and fingers[3]['ang'][0] <= 0.1 \
       and fingers[4]['ang'][0] <= 0.1:
        return True
    else:
        return False

# Detect what the sign is
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
    s.connect((args.host, args.port))
except ConnectionRefusedError:
    print('Connection failed with gloves server')
    sys.exit(1)

try:
    src = read_json_payload(s)['src']
except (KeyError, TypeError):
    pass


sign = 'NOTHING'
while 1:
    data = read_json_payload(s)
    try:
        fingers = data['data']['fingers'];
        old_sign = sign;
        sign = detect_sign(fingers)
        print_fingers(fingers)
        if old_sign != sign and sign != 'NOTHING':
            send_vibration_all(src)
        print(sign)
    except (KeyError, TypeError):
        pass
s.close()
