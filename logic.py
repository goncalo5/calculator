class Count(object):
    def __init__(self, count=''):
        self.count = count

    def add_value(self, value):
        self.count += str(value)

    def evaluate_count(self):
        result = eval(self.count)
        self.count = ''
        return result
