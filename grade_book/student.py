class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def register_for_course(self, course):
        if course not in self.courses_registered:
            self.courses_registered.append(course)

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
            return self.GPA
        total_credits = sum(course.credits for course in self.courses_registered)
        weighted_sum = sum(course.credits * course.grade for course in self.courses_registered)
        self.GPA = weighted_sum / total_credits
        return self.GPA
