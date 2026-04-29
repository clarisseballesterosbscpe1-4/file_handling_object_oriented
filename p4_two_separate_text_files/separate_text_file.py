class NumberProcessor:
    def __init__(self, integers):
        self.integers = integers

    def read_integers(self):
        try:
            with open("integers.txt", "r") as integers_file:
                content = integers.read().split()

                numbers = []
                for item in content:
                    try:
                        numbers.append(int(item))
                    except ValueError:
                        print(f"skipping invalid value: {item}")
                return numbers
        except FileNotFoundError:
            print("input file not found")
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
            if data:
                file.write(" ".join(map(str, data)))
            else:
                file.write("No data")

    def run(self):
        numbers = self.read_integers()

        if not numbers:
            print("No valid numbers to process.")
            return

        even, odd = self.separate_numbers(numbers)

        self.write_file("even.txt", even)
        self.write_file("odd.txt", odd)

        print("Even and Odd numbers successfully written.")
        print(f"Processed {len(numbers)} numbers.")


if __name__ == "__main__":
    app = NumberProcessor("numbers.txt")
    app.run()
