"""Create a new Question class to begin with"""


class Question:
    """Question class"""

    def __init__(self, text, answer):
        """init class with text and answer"""
        self.text = text
        self.answer = answer


if __name__ == "__main__":
    new_q = Question("A slug's blood is green.", "True")
    print(new_q.text)
    print(new_q.answer)
