import socket
import json
import argparse

from sensoglove import SensoGlove
from signs.signs_bank import SignsBank

#improuvement of the sing_matching.py function

parser = argparse.ArgumentParser()
parser.add_argument('glove_host')
parser.add_argument('glove_port', type=int)
parser.add_argument('listener_host')
parser.add_argument('listener_port', type=int)
args = parser.parse_args()

glove = SensoGlove(args.glove_host, args.glove_port)

sb = SignsBank()
sb.load_from_file('signDataBank.dat')

glove.connect()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
socket.settimeout(5)
try:
    socket.connect((args.listener_host, args.listener_port))
except OSError:
    print('Socket connection failed with %s:%d.' % (args.listener_host, args.listener_port))
    raise


old_meaning= 'nothing'
#function who detect sign and compare it
def detection_sign(data):
    matching_sign = sb.compare_with_signs(data)

    if matching_sign is not None and matching_sign.meaning is not old_meaning:
        old_meaning == matching_sign.meaning
        glove.send_vibration(['thumb', 'index', 'middle', 'third', 'little'])
        socket.send((json.dumps({'meaning': matching_sign.meaning}) + '\n').encode())
    print(matching_sign.meaning if sign is not None else None)


while 1:
    glove.fetch_data()
    data = gloves.hand
    detection_sign(data)
