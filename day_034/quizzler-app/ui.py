import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """Quiz Interface class"""

    def __init__(self, quiz_brain: QuizBrain):
        """initialize the quiz interface with all the UI setup up front

        :param quiz_brain: the quiz brain functions
        :type quiz_brain: QuizBrain
        """
        self.quiz_brain = quiz_brain
        # self.score = 0
        self.timer = None

        # main window
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # keep score
        self.lbl_score = tk.Label(
            text=f"Score: {self.quiz_brain.score}", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR
        )
        self.lbl_score.config()
        self.lbl_score.grid(padx=20, pady=20, column=1, row=0)

        # question canvas
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=250, text="Question", font=("Arial", 20, "italic"), fill=THEME_COLOR
        )
        self.canvas.grid(padx=20, pady=20, column=0, row=1, columnspan=2)

        # false button
        img_false = tk.PhotoImage(file="images/false.png")
        self.btn_false = tk.Button(image=img_false, command=self.false_action)
        self.btn_false.grid(padx=20, pady=20, column=0, row=2)

        # true button
        img_true = tk.PhotoImage(file="images/true.png")
        self.btn_true = tk.Button(image=img_true, command=self.true_action)
        self.btn_true.grid(padx=20, pady=20, column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """get the next question from the quiz brain and update the UI"""
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            if self.timer:
                self.window.after_cancel(self.timer)
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have finished the quiz!")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def true_action(self):
        """action when you click the true button"""
        get_it_right = self.quiz_brain.check_answer("True")
        self.give_feedback(get_it_right)

    def false_action(self):
        """action when you click the false button"""
        get_it_right = self.quiz_brain.check_answer("False")
        self.give_feedback(get_it_right)

    def give_feedback(self, is_correct_answer):
        """check the passed in answer and give feedback

        :param is_correct_answer: user answer is correct or no
        :type correct_or_wrong: bool
        """
        if is_correct_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.update_score()
        self.timer = self.window.after(1000, self.get_next_question)

    def update_score(self):
        """update the score label"""
        self.lbl_score.config(text=f"Score: {self.quiz_brain.score}")


if __name__ == "__main__":
    # quiz_brain = QuizBrain()
    # q = QuizInterface(quiz_brain)
    pass
