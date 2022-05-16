from tkinter import *
from quiz_brain import QuizBrain  # it was important to import QuizBrain,
# because this file doesn't now anything about it's datatype(class). So to specify class parameter,
# it is crucial to let our file know what's the class exactly you want to specify in
# __init__ parameters.
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz:QuizBrain): # I've tried to pass the output of the next question method in quiz_brain module
        # straightaway, but it's not possible because object's class is unknown. We want to manipulate object classes
        # whenever we want. - If we would pass the object's method straightaway - we would encounter the problem that
        # that's the only thing we got from the object. And we can't for example, use it's checking ability.
        self.quiz = quiz #Creating a quiz attribute in order to be able to use it(object) everywhere around the class.
        # If we would create it without self, it will be used only here, inside the init function.
        # But if for example we would not use it at all, it would be absolutely the same, we will be able to tap inside
        # only in __init__
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(
            text=f"Score: {0}",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 12)
        )
        self.label_score.grid(row=0, column=1, sticky=E)

        self.new_canvas = Canvas(width=300, height=250)
        self.question_text = self.new_canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text="quiz question text",
            font=("Arial", 15, "italic")
        )
        self.new_canvas.grid(row=1, column=0, columnspan=2, pady=25)

        right_button_img = PhotoImage(file="images/true.png") #no need to make
        # it instance, because we're going to use it only once, in right_button variable.
        # THERE ARE NO OTHER PICTURES EXPECTED.
        self.right_button = Button(
            image=right_button_img,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            relief="flat",
            borderwidth=0,
            command=self.true_button
        )
        self.right_button.grid(row=2, column=0)

        wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(
            image=wrong_button_img,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            relief="flat",
            borderwidth=0,
            command=self.false_button
        )
        self.wrong_button.grid(row=2, column=1)

        self.get_new_question()

        self.window.mainloop()

    def get_new_question(self):
        self.new_canvas.config(bg="white")
        self.label_score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.new_canvas.itemconfig(self.question_text, text=question)
        else:
            self.new_canvas.itemconfig(self.question_text, text="You've finished the quiz.")
            self.right_button.config(state="disable")
            self.wrong_button.config(state="disable")

    def true_button(self):
        is_correct = self.quiz.check_answer("True")
        self.show_result(is_correct)

    def false_button(self):
        is_correct = self.quiz.check_answer("False")
        self.show_result(is_correct)

    def show_result(self, answer):  # this function was made to prevent repetitions, to be able to visually show
        # the result, - from any circumstance. And also make only one method call to get a new question after a
        # button was pressed.
        if answer:
            self.new_canvas.config(bg="green")
        else:
            self.new_canvas.config(bg="red")
        self.window.after(1000, self.get_new_question)

























































    # def get_next_question(self):
    #     self.new_canvas.config(bg="white")
    #     self.label_score.config(text=f"Score: {self.quiz.score}")
    #     if self.quiz.still_has_questions():
    #         self.current_question = self.quiz.next_question()  # to not get any mistakes
    #         self.new_canvas.itemconfig(self.question_text, text=self.current_question)
    #     else:
    #         self.new_canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. "
    #                                                             f"You're score is "
    #                                                             f"{self.quiz.score}/{self.quiz.question_number}")
    #         self.right_button.config(state="disabled")
    #         self.wrong_button.config(state="disabled")

    # def true(self):
    #     button_pressed = "True"
    #     is_correct = self.quiz.check_answer(button_pressed)  # to make code clearer, is correct -
    #     # is not going to be an instance variable,
    #     # so we need to pass it to a give feedback method, and it is more clearer, we're actually passing our
    #     # "is_correct"  boolean to the function, so we understand what's happening. But if we would assign is_correct
    #     # as an instance variable, we won't needed to pass it into the give_feedback function, because as we remember,
    #     # instance variables could be used everywhere inside a function.
    #     self.give_feedback(is_correct)
    #
    # def wrong(self):
    #     button_pressed = "False"
    #     is_correct = self.quiz.check_answer(button_pressed)
    #     self.give_feedback(is_correct)
    #
    # def give_feedback(self, answer:bool):
    #     if answer:
    #         self.new_canvas.config(bg="green")
    #     else:
    #         self.new_canvas.config(bg="red")
    #     self.window.after(1000, self.get_next_question)







