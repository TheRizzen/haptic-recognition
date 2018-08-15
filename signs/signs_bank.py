import pickle

class SignsBank:
    def __init__(self):
        self.signs = []

    def load_from_file(self, filepath):
        try:
            with open(filepath, 'rb') as output_file:
                self.signs = pickle.load(output_file)
        except Exception as e:
            print('Loading signs bank failed:', e)

    def dump_to_file(self, filepath):
        try:
            with open(filepath, 'wb') as input_file:
                pickle.dump(self.signs, input_file)
        except Exception as e:
            print('Dumping signs bank failed: ', e)

    def add_sign(self, sign):
        self.signs.append(sign)

    def compare_with_signs(self, hand):
        for sign in self.signs:
            if sign.compare(hand):
                return sign
        return None
