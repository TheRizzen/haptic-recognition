#!/usr/bin/env python3

from sensoglove import SensoGlove
from signs.signs_bank import SignsBank
import sys
import os

# Improvement of the display_1.py function

# Keep the old meaning
old_meaning = 'nothing'
def detection_sign(data):
        print('\33[102m' + "__________" + '\033[0m')
        # Compare the data with the bank
        detection = sb.compare_with_signs(data)

        # Compare if the sign is not None or not the old meaning and send it
        if  detection is not None:
                if old_meaning is not detectionn.meaning:
                        old_meaning ==  detection.meaning
                        return(detection.meaning)
                else:
                        pass


gloves = SensoGlove('127.0.0.1', 53450)
gloves.connect()

# Initialise the bank function
sb = SignsBank()
# Load a file
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
