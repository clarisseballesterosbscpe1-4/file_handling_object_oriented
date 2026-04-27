class number_processor:
    def __init__(self, input_file):
        self.input_file = input_file

    def read_numbers(self):
        try:
            with open(self.input_file, 'r') as file:
                return list(map(int, file.read().split()))
        except FileNotFoundError:
            print("Input file not found.")
            return []
