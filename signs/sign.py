import math

def compare_thumb(glove_finger, sign_finger):
    pass

def compare_finger(glove_finger, sign_finger):
    result = True
    for i in range(0, 2):
        result &= math.isclose(glove_finger[i], sign_finger[i], abs_tol=0.2)

    return result

class Sign:
    def __init__(self, hand=None, meaning=None):
        self.hand = hand
        self.meaning = meaning

    def compare(self, hand):
        fingers = hand.fingers.data
        result = True
        for i in range(0, len(fingers)):
            if i == 0:
                pass
                #compare_thumb(finger, self.hand.fingers.data[i])
            else:
                result &= compare_finger(fingers[i]['ang'], self.hand.fingers.data[i]['ang'])

        return result
