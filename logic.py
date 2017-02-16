class Count(object):
    def __init__(self, count=''):
        self.count = count

    def add_value(self, value):
        self.count += str(value)

    def evaluate_count(self):
        #print self.count, type(self.count)
        result = eval(self.count)
        return result

    def clear_count(self):
        self.count = ''
