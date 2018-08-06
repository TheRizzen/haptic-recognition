import pickle

class SignsBank:
    def __init__(self, list_test):
        self.signs = list_test

    def load_from_file(self, filepath):
        with open(filepath, 'rb') as output_file:
            self.signs = pickle.load(output_file)

    def dump_to_file(self, filepath):
        with open(filepath, 'wb') as input_file:
            pickle.dump(self.signs, input_file)
