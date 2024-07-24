from gradebook import GradeBook
from student import Student
from course import Course

def main():
    gradebook = GradeBook()

    while True:
        print("Welcome to Ewing's Grade Book Application")
        print('Please select an option: ')
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(Student(email, names))
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            gradebook.add_course(Course(name, trimester, credits))
        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(email, course_name, grade)
        elif choice == '4':
            ranking = gradebook.calculate_ranking()
            for email, gpa in ranking:
                print(f"{email}: {gpa}")
        elif choice == '5':
            grade = float(input("Enter grade to search for: "))
            students = gradebook.search_by_grade(grade)
            print("Students with grade", grade, ":", students)
        elif choice == '6':
            email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(email)
            print(transcript)
        elif choice == '7':
            break
        else:
             print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()