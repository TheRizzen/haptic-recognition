#!/usr/bin/env python3

from sensoglove import SensoGlove
import sys
import os
import time

#addaptation of the display_1.py function for web

gloves = SensoGlove('192.168.56.101', 53450)
gloves.connect()

sign = 'Nothing'



def detection_test(data):
        #print ('thumb:')
        # print(data.thumb.pitch)
        # print(data.thumb.roll)
        # print(data.thumb.yaw)

        print('\33[93m' + "index" + '\033[0m')
        print ('index:')
        print(data.index.pitch)
        print(data.index.roll)
        print(data.index.yaw)

        print('\33[91m' + "middle" + '\033[0m')
        print(data.middle.pitch)
        print(data.middle.roll)
        print(data.middle.yaw)

        print('\33[92m' + "third" + '\033[0m')
        print(data.third.pitch)
        print(data.third.roll)
        print(data.third.yaw)

        print('\33[94m' + "little" + '\033[0m')
        print(data.little.pitch)
        print(data.little.roll)
        print(data.little.yaw)


def vibration():
        gloves.send_vibration(gloves.hand.fingers.thumb,655, 10)
        gloves.send_vibration(gloves.hand.fingers.index,655, 10)
        gloves.send_vibration(gloves.hand.fingers.middle,655, 10)
        gloves.send_vibration(gloves.hand.fingers.third,655, 10)
        gloves.send_vibration(gloves.hand.fingers.little,655, 10)

prev = 0
def detection_sign(data):
    global prev
    if data.index.pitch <= 0.5 \
       and data.middle.pitch <= 0.5 \
       and data.third.pitch >= 2 \
       and data.little.pitch >=2\
       and prev != 1:
        prev = 1
        return ('Ninja')

    elif data.index.pitch  >= 2 \
       and data.middle.pitch  >= 2 \
       and data.third.pitch >= 2 \
       and data.little.pitch >=2\
       and prev != 2:
        prev = 2
        return ('Rock')
    else:
        return ('RIEN')



count = 0


def displayData():
        #print('\33[102m' + "__________" + '\033[0m')

        gloves.fetch_data()

        try:
            data = gloves.hand.fingers
            #sign =  detection_test(data)
            sign =  detection_sign(data)
            #count += 1
            print(sign)

        except (KeyError, TypeError):
            pass
        return sign

#send the sign to the web client
def displayToClient():
    bite = displayData()
    print("sign: ")
    print(sign)

    time.sleep(1)
    return bite
