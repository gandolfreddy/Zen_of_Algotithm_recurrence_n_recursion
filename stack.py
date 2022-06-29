'''
    Build a stack with the built-in list
'''


class Stack:
    def __init__(self):
        self.stk = []

    def push(self, val):
        self.stk.append(val)

    def pop(self):
        return self.stk.pop()

    def is_empty(self):
        return len(self.stk) == 0

    def peek(self):
        return self.stk[-1]

    def size(self):
        return len(self.stk)