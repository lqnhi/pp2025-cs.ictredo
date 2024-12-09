
students = []
courses = []
marks = {}


def input_students():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        sid = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students.append((sid, name, dob))

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        cid = input("Enter course ID: ")
        cname = input("Enter course name: ")
        courses.append((cid, cname))

def input_marks():
    course_id = input("Enter course ID: ")
    if course_id not in [c[0] for c in courses]:
        print("Course not found!")
        return
    if course_id not in marks:
        marks[course_id] = {}
    for student in students:
        mark = float(input(f"Enter mark for {student[1]} (ID: {student[0]}): "))
        marks[course_id][student[0]] = mark

def list_students():
    print("\nStudents:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def list_courses():
    print("\nCourses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def show_marks():
    course_id = input("Enter course ID to view marks: ")
    if course_id not in marks:
        print("No marks for this course.")
        return
    print(f"\nMarks for course {course_id}:")
    for sid, mark in marks[course_id].items():
        student_name = next(s[1] for s in students if s[0] == sid)
        print(f"Student: {student_name}, Mark: {mark}")


def menu():
    while True:
        print("\nMenu:")
        print("1. Add students")
        print("2. Add courses")
        print("3. Add marks")
        print("4. Show students")
        print("5. Show courses")
        print("6. Show marks")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

menu() 