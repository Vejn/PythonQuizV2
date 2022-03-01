from tkinter import *

THEME_COLOR = "#375362"


# Building user interface with Tkinter
class QuizInterface:

    def __init__(self, quiz_brain):
        # Creating Quiz and Window
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Creating Canvas where the question will be displayed
        self.canvas = Canvas(width=300, height=250)
        self.q_text = self.canvas.create_text(150, 125, text="Some Question", font=("Arial", 15, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Creating True Button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=1, row=2)

        # Creating False Button
        x_image = PhotoImage(file="images/false.png")
        self.x_button = Button(image=x_image, highlightthickness=0, command=self.false_answer)
        self.x_button.grid(column=0, row=2)

        # Creating Label to display Score
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.get_next_question()
        self.window.mainloop()

    # Defining Methods to check answer and get next question
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the Quiz!")
            self.true_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    # Creating Method for giving Feedback to the Player
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




