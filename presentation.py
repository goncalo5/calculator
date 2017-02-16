from Tkinter import *
from constants import *
from logic import Count

class Menu(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')

        self.c = Count()

        # screen
        self.l_screen = Label(self.root, text="")
        self.l_screen.grid(row=0, column=0, rowspan=2, columnspan=4)

        # buttons
        # numbers
        Button(text='0', command=lambda *args: self.print_number('0')).grid(row=6, column=0)
        number = 1
        for i in xrange(5, 2, -1):
            for j in xrange(0, 3):
                Button(text=str(number),
                    command=lambda number=number: self.print_number(number)).grid(row=i, column=j)
                number = int(number)
                number += 1

        # others
        Button(text='=', padx=30, command=self.equal).\
            grid(row=SYMBOLS['='][0], column=SYMBOLS['='][1], columnspan=2)
        for name in OPERATORS:
            Button(text=name, command=lambda name=name: self.print_number(name)).\
                    grid(row=OPERATORS[name][0], column=OPERATORS[name][1])

        self.root.mainloop()

    def equal(self):
        self.clear_screen()
        self.print_result()
        self.c.clear_count()

    def clear_screen(self):
        self.l_screen['text'] = ''

    def print_number(self, number):
        number = str(number)
        print self.l_screen['text'], type(self.l_screen['text']), type(number)
        self.l_screen['text'] += number
        self.c.add_value(number)

    def print_result(self):
        self.l_screen['text'] = str(self.c.evaluate_count())
