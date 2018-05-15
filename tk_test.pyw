try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

QUESTIONS = (
    ('What is the airspeed velocity of an unladen swallow?', (
        'A. 9 m/s',
        'B. 10 m/s',
        'C. 11 m/s',
        'D. What do you mean? African or European swallow?',
        3
    )),
    ('Why is it blue?', (
        'A. Why not?',
        'B. Because I like blue.',
        'C. How should I know?',
        0
    )),
    ('What is the capital of Assyria?', (
        'A. Oman',
        'B. Assur',
        'C. Brisbane',
        'D. The Pentagon',
        1
    )),
    ('What is the radius of an circle tangent to four radius 1 corner circles of a radius 1 square?', (
        'A. 1',
        'B. tan(3)',
        'C. sqrt(2) - 1',
        'D. pi',
        2
    ))
)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.done_button = tk.Button(self, text='Choose', command=self.chosen)
        self.done_button.pack(side='top')
        self.question_index = 0
        self.question = tk.Label(self, text=QUESTIONS[
            self.question_index
        ][0])
        self.question.pack(side='top')
        self.choices = tk.Listbox(self, width=60)
        self.choices.insert('end', *QUESTIONS[self.question_index][1][:-1])
        self.choices.pack(side='bottom')

    def chosen(self):
        choice = self.choices.curselection()[0]
        if QUESTIONS[self.question_index][1][-1] == choice:
            # correct
            try:
                self.question_index += 1
                self.question['text'] = QUESTIONS[self.question_index][0]
                self.choices.delete(0, len(QUESTIONS[self.question_index][1]) - 1)
                self.choices.insert('end', *QUESTIONS[self.question_index][1][:-1])
            except IndexError:
                self.choices.destroy()
                self.done_button.destroy()
                self.yay = tk.Button(self, text='Bye!', command=root.destroy)
                self.yay.pack(side='bottom')
                self.question['text'] = 'You completed all the questions!'
        else:
            self.question['text'] = 'INCORRECT. Try again.\n' + self.question['text']


root = tk.Tk()
app = App(master=root)
app.mainloop()
