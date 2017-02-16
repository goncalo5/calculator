def add_number(number):
    print number


class Count(object):
    def __init__(self, count=''):
        self.count = count

    def add_number(self, number):
        print number

    def evaluate_count(self):
        print self.count
