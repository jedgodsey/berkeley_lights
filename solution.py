class Interval:
    def __init__(self, start, end=None):
        self.start = start
        self.end = end or start

test = Interval(5)

test.string = 'goober'

print(test.end)
