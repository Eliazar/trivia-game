from tkinter import *
from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

THEME_COLOR = "#375362"


class QuizInterface:

    __score: int = 0
    __questionBank = []

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        label = Label(text=f"Score: {self.__score}", background=THEME_COLOR, foreground="white",
                      font=("arial", 9))
        label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(self.window, height=250, width=300)
        self.canvas.config(highlightthickness=0)
        self.question = self.canvas.create_text(
            150, 125, text="", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        trueImage = PhotoImage(file="images/true.png")
        trueButton = Button(
            image=trueImage, highlightthickness=0, command=self.selectedTrue)
        trueButton.grid(row=2, column=0, pady=20, padx=20)

        falseImage = PhotoImage(file="images/false.png")
        falseButton = Button(
            image=falseImage, highlightthickness=0, command=self.selectedFalse)
        falseButton.grid(row=2, column=1, pady=20, padx=20)

        self.__setQuestionBank()

        self.window.mainloop()

    def __setQuestionBank(self):
        for question in question_data:
            question_text = question.get("question")
            question_answer = question.get("correct_answer")
            new_question = Question(question_text, question_answer)
            self.__questionBank.append(new_question)

        self.quiz = QuizBrain(self.__questionBank)
        self.getQuestion()

    def getQuestion(self):
        if (self.quiz.still_has_questions()):
            nextQuestion = self.quiz.next_question()
            self.canvas.itemconfig(
                self.question, text=f"{nextQuestion}", fill=THEME_COLOR)

    def selectedTrue(self):
        pass

    def selectedFalse(self):
        pass
