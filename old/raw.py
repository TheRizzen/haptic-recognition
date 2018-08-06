#!/usr/bin/env python3

import sys
import socket
import json
import os
import argparse
import time

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
        print('ERROR')
        pass

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.host, args.port))
    s.settimeout(1)
except ConnectionRefusedError:
    print('Connection failed with gloves server')
    sys.exit(1)

try:
    src = read_json_payload(s)['src']
except (KeyError, TypeError):
    pass


while 1:
    try:
        data = read_json_payload(s)
        print(data)
    except (KeyError, TypeError):
        pass

s.close()
