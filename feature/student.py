class StudentProfile:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.__total_score = 0

    def add_points(self, points_earned):
        if points_earned < 0:
            print("Cannot add negative values")
        else:
            self.__total_score += points_earned
            pass

    def get_current_score(self):
             return self.__total_score