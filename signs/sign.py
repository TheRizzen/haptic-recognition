import math

PITCH_FINGER_COMPARISON_SENSIBILITY = 0.2
YAW_FINGER_COMPARISON_SENSIBILITY = 0.1

def compare_finger(glove_finger, sign_finger):
    sensibilities = [PITCH_FINGER_COMPARISON_SENSIBILITY, YAW_FINGER_COMPARISON_SENSIBILITY]
    for i in range(0, 2):
        if not math.isclose(glove_finger[i], sign_finger[i], abs_tol=sensibilities[i]):
            return False

    return True

class Sign:
    def __init__(self, hand=None, meaning=None):
        self.hand = hand
        self.meaning = meaning

    def compare(self, hand):
        fingers = hand.fingers.data
        for i in range(0, len(fingers)):
            if not compare_finger(fingers[i]['ang'], self.hand.fingers.data[i]['ang']):
                return False

        return True
