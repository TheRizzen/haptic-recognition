import pickle

#bank sign of finger

class SignsBank:
    def __init__(self):
        self.signs = []

    #load sign from a bnak file
    def load_from_file(self, filepath):
        try:
            #open the file in read mode
            with open(filepath, 'rb') as output_file:
                self.signs = pickle.load(output_file)
        except Exception as e:
            print('Loading signs bank failed:', e)

    #file the file with the sign
    def dump_to_file(self, filepath):
        try:
            #writ in the file
            with open(filepath, 'wb') as input_file:
                pickle.dump(self.signs, input_file)
        except Exception as e:
            print('Dumping signs bank failed: ', e)

    #add sign
    def add_sign(self, sign):
        self.signs.append(sign)

   #compare sign 
    def compare_with_signs(self, hand):
        for sign in self.signs:
            if sign.compare(hand):
                return sign
        return None
