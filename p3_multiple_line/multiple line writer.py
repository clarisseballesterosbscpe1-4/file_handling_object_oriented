class life_writer:
    def __init__(self, my_life):
        self.my_life = my_life

    def write_lines(self):
        file = open(self.my_life, "w")

        while True:
            line = input("Enter your line: ")
            file.write(line + "\n")

            choice = input("Add more? (y/n): ")

            if choice != "y":
                break

            file.close()
            print("File saved.")

app = life_writer("my_life.txt")
app.write_lines()