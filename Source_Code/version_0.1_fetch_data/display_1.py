#!/usr/bin/env python3

from sensoglove import SensoGlove
from signs.signs_bank import SignsBank
import sys
import os

#function display who check sign and print dirrectly the sign found


#connection de the gloves with the server and the port of the glove, available on the SensoUi
#and create a object gloves
gloves = SensoGlove('127.0.0.1', 53450)
gloves.connect()

#function who print the data reciev from the gloves for each finger (withou the thrumb)
def detection_test(data):

        print('\33[93m' + "index" + '\033[0m')
        print ('index:')
        print(data.index.pitch) #print the pitch
        print(data.index.roll)  #print the roll
        print(data.index.yaw)   #print the yaw

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

#var to check if the old signs is same or different
prev = 0
def detection_sign(data):
    global prev
    #hand possiton for a signe
    if data.index.pitch <= 0.5 \
       and data.middle.pitch <= 0.5 \
       and data.third.pitch >= 2 \
       and data.little.pitch >=2\
       and prev != 1: #if different from the previous signe
        prev = 1
        return ('Ninja') # return the sign detected

    elif data.index.pitch  >= 2 \
       and data.middle.pitch  >= 2 \
       and data.third.pitch >= 2 \
       and data.little.pitch >=2\
       and prev != 2:
        prev = 2
        return ('Rock')
    else:
        return ('RIEN')


#send vibration to fingers
def vibration():
        #send a vibration to a finger, for how long in second and the strengh of the fibration
        gloves.send_vibration(gloves.hand.fingers.thumb,655, 10)
        gloves.send_vibration(gloves.hand.fingers.index,655, 10)
        gloves.send_vibration(gloves.hand.fingers.middle,655, 10)
        gloves.send_vibration(gloves.hand.fingers.third,655, 10)
        gloves.send_vibration(gloves.hand.fingers.little,655, 10)


sign = 'Nothing'
while 1:
        #reciev the data from the gloves
        gloves.fetch_data()

        try:
                #initialise data as a shortcut for the object gloves.hand
                data = gloves.hand
                #send the object to the fonction to detect sign
                sign = detection_sign(data)
                #print the sign detected
                print(sign)
        except (KeyError, TypeError):
                pass
