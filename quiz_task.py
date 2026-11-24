from base_task import AcademicTask

class Quiz(AcademicTask):
    def __init__(self, title, max_points, total_questions):
        super().__init__(title, max_points)
        self.__total_questions__ = total_questions
        self.correct_answers = 0

def (self, submit_work)