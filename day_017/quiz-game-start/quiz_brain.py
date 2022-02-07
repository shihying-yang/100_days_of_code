"""QuizBrain class"""


from multiprocessing.dummy import current_process


class QuizBrain:
    """QuizBrain class"""

    def __init__(self, question_list):
        """[summary]"""
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        """ask the next question"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text}  (True/False)?: ")
        self.check_answer(answer, current_question)

    def still_has_question(self):
        """check if there are still more questions"""
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, question):
        """check the user answer against the correct answer"""
        if answer.lower().startswith("t") or answer.lower().startswith("y"):
            answer = "True"
        else:
            answer = "False"

        if answer == question.answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {question.answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
