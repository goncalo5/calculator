from Tkinter import *
from constants import *
from logic import add_number

class Menu(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')

        # buttons
        # numbers
        Button(text='0', command=lambda *args: add_number('0')).grid(row=6, column=0)
        number = 1
        for i in xrange(5, 2, -1):
            for j in xrange(0, 3):
                Button(text=str(number),
                    command=lambda number=number: add_number(number)).grid(row=i, column=j)
                number += 1

        # others
        Button(text='=', padx=10, command=lambda: add_number('=')).grid(row=6, column=2, columnspan=2)
        for name in SYMBOLS:
            Button(text=name,
                    command=lambda name=name: add_number(name)).grid(row=SYMBOLS[name][0], column=SYMBOLS[name][1])

        self.root.mainloop()
