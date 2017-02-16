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
                number += 1

        # others
        Button(text='=', padx=10, command=self.print_result).grid(row=6, column=2, columnspan=2)
        for name in SYMBOLS:
            Button(text=name, command=lambda name=name: self.c.add_value(name)).\
                    grid(row=SYMBOLS[name][0], column=SYMBOLS[name][1])

        self.root.mainloop()

    def print_number(self, number):
        self.l_screen['text'] = number
        self.c.add_value(number)

    def print_result(self):
        self.l_screen['text'] = self.c.evaluate_count()
