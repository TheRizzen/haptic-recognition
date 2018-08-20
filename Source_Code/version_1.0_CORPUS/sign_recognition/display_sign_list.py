import sys
import os
import argparse

from signs.signs_bank import SignsBank
from signs.sign import Sign

parser = argparse.ArgumentParser()
parser.add_argument('bank_file')
args = parser.parse_args()

bank = SignsBank()

# Print all the meaning in the bank file
bank.load_from_file(args.bank_file)
#print(bank.signs)
for sign in bank.signs:
    print(sign.meaning)
