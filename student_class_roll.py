class Student:
    def __init__(self, name, roll_number, subject, marks):
        self.name = name
        self.roll_number = roll_number
        self.subject = subject
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        elif self.marks >= 50:
            return 'E'
        else:
            return 'F'

def main():
    # Creating an instance of the Student class
    Ahsan_Iqbal = Student(name="Ahsan Iqbal", roll_number="2023110", subject="Object Oriented Programing", marks=89)

    # Displaying student information
    print(f"Student Name: {Ahsan_Iqbal.name}")
    print(f"Roll Number: {Ahsan_Iqbal.roll_number}")
    print(f"Subject: {Ahsan_Iqbal.subject}")
    print(f"Marks: {Ahsan_Iqbal.marks}")
    print(f"Grade: {Ahsan_Iqbal.calculate_grade()}")

if __name__ == "__main__":
    main()
