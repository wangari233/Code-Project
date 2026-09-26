students = [{"name":"Rita", "age": 20, "course": "Cyber Security", "marks": 90},
            {"name": "Kevin", "age": 35, "course": "Software Engineering", "marks": 85},
            {"name": "Joseph", "age": 26, "course": "Computer Science", "marks":80},
            {"name": "Sammy", "age": 36, "course": "Data Science", "marks": 75},
            {"name": "Cecil", "age": 40, "course": "Accounting", "marks": 70}]

def display_all_students():
    print("\nAll Students")
    if not students:
        print("No students found")
        return
    for index, student in enumerate(students,1):
     print(f"{index}. Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Marks: {student['marks']}")

def find_student_by_name():
    name = input("\nEnter student name to search:").strip()
    for student in students:
        if student['name'].lower()==name.lower():
            print(f"\nFound: Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Marks: {student['marks']}")

def calculate_average_mark():
    if not students:
        print("\nNo average marks were calculated.")
        return
    total = sum(student['marks'] for student in students)
    average = total / len(students)
    print(f"\nAverage marks of all students:{average:.2f}")

def find_highest_mark():
    if not students:
        print("\nNo students are available.")
        return
    top_student = students[0]
    for student in students:
        if student['marks'] > top_student['marks']:
            top_student = student
        print("\nStudent with highest marks:")
        print(f"Name: {top_student['name']}, Age: {top_student['age']}, Course: {top_student['course']}, Marks: {top_student['marks']}")     

def find_lowest_mark():
    if not students:
        print("\nNo students are available.")
        return
    lowest_student = students[0]
    for student in students:
        if student['marks'] < lowest_student['marks']:
            lowest_student = student
        print("\nStudent with lowest marks:") 
        print(f"Name: {lowest_student['name']}, Age: {lowest_student['age']}, Course: {lowest_student['course']}, Marks: {lowest_student['marks']}") 

def main():
    while True:
        print("\nStudent Management System")
        print("1. Display All Students")
        print("2. Find Student by Name")
        print("3. Calculate Average Mark")
        print("4. Find Student with Highest Mark")
        print("5. Find Student with Lowest Mark")
        print("6. Exit")
        choice = input("Enter your choice(1-6):").strip()
        if choice == "1":
            display_all_students()
        elif choice == "2":
            find_student_by_name()
        elif choice == "3":
            calculate_average_mark()
        elif choice == "4":
            find_highest_mark()
        elif choice == "5":
            find_lowest_mark()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6. ")

if __name__ == "__main__":
    main()        