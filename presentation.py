from Tkinter import *
from constants import *
from logic import Count

class Menu(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')

        self.canvas = Canvas(self.root, width=L_SCREEN, height=H_SCREEN)
        self.canvas.focus_force()
        self.canvas.grid(columnspan=4)
        self.canvas.bind('<Key>', self.write)

        self.c = Count()

        # screen
        self.l_screen = Label(self.root, text="")
        self.l_screen.grid(row=0, column=0, rowspan=2, columnspan=4)

        # buttons
        # numbers
        Button(text='0', command=lambda *args: self.print_value('0')).grid(row=6, column=0)
        number = 1
        for i in xrange(5, 2, -1):
            for j in xrange(0, 3):
                Button(text=str(number),
                    command=lambda number=number: self.print_value(number)).grid(row=i, column=j)
                number = int(number)
                number += 1

        # others
        symb = '='
        Button(text=symb, padx=30, command=self.equal).\
            grid(row=SPECIAL[symb][0], column=SPECIAL[symb][1], columnspan=2)
        symb = 'AC'
        Button(text=symb, command=self.ac).\
            grid(row=SPECIAL[symb][0], column=SPECIAL[symb][1])
        for name in SYMBOLS:
            Button(text=name, command=lambda name=name: self.print_value(name)).\
                    grid(row=SYMBOLS[name][0], column=SYMBOLS[name][1])

        self.root.mainloop()

    def write(self, event):
        op = {'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/', 'period': '.'}
        char = event.keysym
        if char == '??':
            return
        elif char == 'Return':
            self.equal()
        elif char == 'BackSpace':
            self.ac()
        else:
            if char in op:
                char = op[char]
            self.print_value(char)

    # buttons methods
    def print_value(self, value):
        value = str(value)
        #print self.l_screen['text'], type(self.l_screen['text']), type(number)
        if self.c.count == '':
            self.clear_screen()
        self.l_screen['text'] += value
        self.c.add_value(value)

    def equal(self):
        self.clear_screen()
        self.print_result()
        self.c.clear_count()

    def ac(self):
        self.clear_screen()
        self.c.clear_count()

    # Auxiliary methods
    def clear_screen(self):
        self.l_screen['text'] = ''

    def print_result(self):
        self.l_screen['text'] = str(self.c.evaluate_count())
