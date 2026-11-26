from base_task import AcademicTask

class Essay(AcademicTask):

    def __init__(self, title, max_points, minimum_words):
        super().__init__(title, max_points)
        self.__minimum_words = minimum_words

        self.submitted_word_count = 0

    def submit_work(self, word_count):
        self.submitted_word_count = word_count
        print(f"Essay submitted: {self.title}")

    def grade_work(self):
        if self.submitted_word_count >= self.__minimum_words:
            grade = self.max_points
        else:
            grade = self.max_points - (self.max_points * 0.20)
            
        self.is_graded = True
        return grade

    def get_details(self):
        print(f"[ESSAY] {self.title} - Max Points: {self.max_points}")

