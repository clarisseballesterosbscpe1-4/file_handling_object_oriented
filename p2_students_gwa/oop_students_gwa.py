class students_gwa:
    def __init__(self, students):
        self.students = students

    def read_students(self):
        students = []
        try:
            with open (self.students, 'r') as file:
                for line in file:
                    name, gwa = line.split()
                    students.append((name, (gwa)))
        except FileNotFoundError:
            print("File not found")
        return students
    def find_student(self, students):
        if not students:
            return None

        best_gwa = students[0][1]

        for student in students:
            if student[1] == best_gwa:
                best_gwa = student[1]

        top_student = []
        for student in students:
            if student[1] == best_gwa:
                top_student.append(student)
        return top_student

    def run(self):
        students = self.read_students()
        top = self.find_student(students)

        top = self.find_student(students)

        if top:
            print("Top Students:")
            for student in top:
                print(student[0], "with GWA", student[1])
        else:
            print("No top student")

if __name__ == "__main__":
    app = students_gwa("students.txt")
    app.run()