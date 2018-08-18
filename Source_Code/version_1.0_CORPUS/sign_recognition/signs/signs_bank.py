import pickle

# Bank sign of finger

class SignsBank:
    def __init__(self):
        self.signs = []

    # Load sign from a bank file
    def load_from_file(self, filepath):
        try:
            # Open the file in read mode
            with open(filepath, 'rb') as output_file:
                self.signs = pickle.load(output_file)
        except Exception as e:
            print('Loading signs bank failed:', e)

    # Fille the file with the sign
    def dump_to_file(self, filepath):
        try:
            # Write in the file
            with open(filepath, 'wb') as input_file:
                pickle.dump(self.signs, input_file)
        except Exception as e:
            print('Dumping signs bank failed: ', e)

    # Add sign
    def add_sign(self, sign):
        self.signs.append(sign)

   # Compare sign
    def compare_with_signs(self, hand):
        for sign in self.signs:
            if sign.compare(hand):
                return sign
        return None
