import json
import argparse

from sensoglove import SensoGlove
from signs.signs_bank import SignsBank

#light version of the sign_matcking.py function whitout the socket and communication with the web interface and serveur

parser = argparse.ArgumentParser()
parser.add_argument('glove_host')
parser.add_argument('glove_port', type=int)
args = parser.parse_args()

glove = SensoGlove(args.glove_host, args.glove_port)
sb = SignsBank()
sb.load_from_file('hugo.dat')

glove.connect()

old_meaning= 'nothing'
def detection_sign(data):
    matching_sign = sb.compare_with_signs(data)

    if matching_sign is not None and old_meaning is not matching_sign.meaning:
            old_meaning == matching_sign.meaning
            glove.send_vibration(['thumb', 'index', 'middle', 'third', 'little'])
    print(matching_sign.meaning if matching_sign is not None else None)

while 1:
    glove.fetch_data()
    data = glove.hand
    detection_sign(data)
