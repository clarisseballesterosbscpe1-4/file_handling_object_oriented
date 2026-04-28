class students_gwa:
    def __init__(self, students):
        self.students = students

    def read_students(self):
        students = []
        try:
            with open (self.students, 'r') as file:
                for line in file:
                    name, gwa = line.split()
                    students.append((name, float(gwa)))
        except FileNotFoundError:
            print("File not found")
        return students

    def find_student(self, students):
        if not students:
            return None
        return min(students, key=lambda x: x[1])