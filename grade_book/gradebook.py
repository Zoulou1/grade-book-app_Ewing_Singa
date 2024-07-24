class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course)
            course.grade = grade

    def calculate_ranking(self):
        sorted_students = sorted(self.student_list, key=lambda s: s.calculate_GPA(), reverse=True)
        return [(student.email, student.GPA) for student in sorted_students]

    def search_by_grade(self, grade):
        return [student.email for student in self.student_list if any(course.grade == grade for course in student.courses_registered)]

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            transcript = f"Student: {student.names}\nEmail: {student.email}\nGPA: {student.GPA}\nCourses:\n"
            for course in student.courses_registered:
                transcript += f"{course.name} - Grade: {course.grade}\n"
            return transcript
        return "Student not found"