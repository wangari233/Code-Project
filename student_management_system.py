import json
from unicodedata import name
FILE = "students.json"

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = {}

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = []

    def add_mark(self, course_name, mark):   
        if course_name in self.courses:
                self.courses[course_name].append(mark)

    def average_mark(self, course_name):
        marks = self.courses.get(course_name, [])
        return sum(marks) / len(marks) if marks else 0

    def overall_average(self):
        all_marks = [mark for marks in self.courses.values() for mark in marks]
        return sum(all_marks) / len(all_marks) if all_marks else 0

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "courses": self.courses
        }

    @staticmethod
    def from_dict(data):
        student = Student(data["name"], data["age"])
        student.courses = data.get("courses", {})
        return student

class StudentManager:
    def __init__(self):
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(FILE, "r") as file:
                return [Student.from_dict(student_data) for student_data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self):
        with open(FILE, "w") as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add_student(self, name, age):
        student = Student(name, age)
        self.students.append(student)
        self.save_students()

    def view_students(self):
        for s in self.students:
            print(f"Name: {s.name}, Age: {s.age}, Courses: {list(s.courses.keys())}")

    def search_student(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                return s
        return None

    def update_student(self, name, new_age):
        student = self.search_student(name)
        if student:
            student.age = new_age
            self.save_students()

    def delete_student(self, name):
        self.students = [s for s in self.students if s.name.lower() != name.lower()]
        self.save_students()

    def highest_student(self):
        return max(self.students, key=lambda s: s.overall_average(), default=None)

    def lowest_student(self):
        return min(self.students, key=lambda s: s.overall_average(), default=None)

def main():
    manager = StudentManager()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View all Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Course to Student")
        print("7. Record Marks for Student")
        print("8. Calculate Average Marks")
        print("9. Highest Scoring Student")
        print("10. Lowest Scoring Student")
        print("11. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            manager.add_student(name, age)
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            name = input("Enter student name to search: ")
            student = manager.search_student(name)
            print(student if student else "Student not found.")
        elif choice == "4":
            name = input("Enter student name to update: ")
            new_age = int(input("Enter new age: "))
            manager.update_student(name, new_age)
        elif choice == "5":
            name = input("Enter student name to delete: ")
            manager.delete_student(name)
        elif choice == "6":
            name = input("Enter student name:")
            course = input("Enter course name: ")
            mark = float(input("Enter mark: "))
            student = manager.search_student(name)
            if student:
                student.add_course(course)
                manager.save_students()
        elif choice == "7":
            name = input("Enter student name to record marks: ")
            course = input("Enter course name: ")
            mark = float(input("Enter mark: "))
            student = manager.search_student(name)
            if student:
                student.add_mark(course, mark)
                manager.save_students()
        elif choice == "8":
            name = input("Enter student name:")
            course = input("Enter course name:")
            student = manager.search_student(name)
            if student:
                avg = student.average_mark(course)
                print(f"Average marks for {name} in {course}: {avg}")
        elif choice == "9":
            student =manager.highest_student()
            print(f"Highest scoring student: {student.to_dict()}" if student else "No students found.")
        elif choice == "10":
            student = manager.lowest_student()
            print(f"Lowest scorin student: {student.to_dict()}" if student else "No students found.")
        elif choice == "11":
            print("Exiting...")
            break    
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
