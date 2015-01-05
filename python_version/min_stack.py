class stack:
    def __init__(self):
        self.s = []


    def push(self, val):
        self.s.append(val)

    def pop(self):
        return self.s.pop()

    def top(self):
        return self.s[-1]



class MinStack:
    def __init__(self):
        self.s = stack()
        self.min_s = stack()

    def push(self, val):
        if len(self.min_s.s) == 0 or val <= self.min_s.top(): # BUG PRONE, Here must use <=, instead of <
            self.min_s.push(val)

        self.s.push(val)

    def pop(self):
        if self.s.top() == self.min_s.top():
            self.min_s.pop()
        return self.s.pop()


    def getMin(self):
        return self.min_s.top()


    def top(self):
        return self.s.top()