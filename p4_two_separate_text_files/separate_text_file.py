class NumberProcessor:
    def __init__(self, integers):
        self.integers = integers

    def read_integers(self):
        with open("integers.txt", "r") as integers_file:
            numbers =  integers_file.read().split()
