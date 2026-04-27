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

    def separate_numbers(self, numbers):
        even = []
        odd = []

        for num in numbers:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return even, odd

    def write_file(self, filename, data):
        with open(filename, 'w') as file:
            file.write(" ".join(map(str, data)))
    