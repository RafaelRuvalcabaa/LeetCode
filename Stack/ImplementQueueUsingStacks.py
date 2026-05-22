class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if self.stack2 != []:
            return self.stack2.pop()
        while self.stack1 != []:
            first = self.stack1.pop()
            self.stack2.append(first)
        return self.stack2.pop()

    def peek(self):
        if self.stack2 != []:
            return self.stack2[-1]
        while self.stack1 != []:
            first = self.stack1.pop()
            self.stack2.append(first)
        return self.stack2[-1]

    def empty(self):
        if self.stack1 == [] and self.stack2 == []:
            return True
        else:
            return False
