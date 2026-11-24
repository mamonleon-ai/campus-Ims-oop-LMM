from base_task import AcademicTask

class Quiz(AcademicTask):
    def __init__(self, title, max_points, total_questions):
        super().__init__(title, max_points)
        self