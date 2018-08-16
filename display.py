#!/usr/bin/env python3

from sensoglove import SensoGlove
from signs.signs_bank import SignsBank
import sys
import os

# gloves = SensoGlove('127.0.0.1', 53450)
# gloves.connect()

# sb = SignsBank()
# sb.load_from_fille('test.dat')

# sign = 'Nothing'



# def detection_test(data):
#         #print ('thumb:')
#         # print(data.thumb.pitch)
#         # print(data.thumb.roll)
#         # print(data.thumb.yaw)

#         print('\33[93m' + "index" + '\033[0m')
#         print ('index:')
#         print(data.index.pitch)
#         print(data.index.roll)
#         print(data.index.yaw)

#         print('\33[91m' + "middle" + '\033[0m')
#         print(data.middle.pitch)
#         print(data.middle.roll)
#         print(data.middle.yaw)

#         print('\33[92m' + "third" + '\033[0m')
#         print(data.third.pitch)
#         print(data.third.roll)
#         print(data.third.yaw)

#         print('\33[94m' + "little" + '\033[0m')
#         print(data.little.pitch)
#         print(data.little.roll)
#         print(data.little.yaw)


# def vibration():
#         gloves.send_vibration(gloves.hand.fingers.thumb,655, 10)
#         gloves.send_vibration(gloves.hand.fingers.index,655, 10)
#         gloves.send_vibration(gloves.hand.fingers.middle,655, 10)
#         gloves.send_vibration(gloves.hand.fingers.third,655, 10)
#         gloves.send_vibration(gloves.hand.fingers.little,655, 10)


old_meaning = 'nothing'
def detection_sign(data):
        print('\33[102m' + "__________" + '\033[0m')
        detection = sb.compare_with_signs(data)

        if  detection is not None:
                if old_meaning is not detectionn.meaning:
                        old_meaning ==  detection.meaning
                        return(detection.meaning)
                else:
                        pass

                
gloves = SensoGlove('127.0.0.1', 53450)
gloves.connect()

sb = SignsBank()
sb.load_from_fille('test.dat')

sign = 'Nothing'
while 1:
        gloves.fetch_data()

        try:
                data = gloves.hand
                sign = detection_sign(data)
                print(sign)
        except (KeyError, TypeError):
                pass
