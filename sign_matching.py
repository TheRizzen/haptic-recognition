from sensoglove import SensoGlove
from signs.signs_bank import SignsBank

glove = SensoGlove('192.168.33.2', 53451)

sb = SignsBank()
sb.load_from_file('voc1.dat')

glove.connect()

sign = None
while 1:
    glove.fetch_data()
    matching_sign = sb.compare_with_signs(glove.hand)
    if matching_sign is not None and matching_sign is not sign:
        sign = matching_sign
        glove.send_vibration(['thumb', 'index', 'middle', 'third', 'little'])
    print(sign.meaning if sign is not None else None)
