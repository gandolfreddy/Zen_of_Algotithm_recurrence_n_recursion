'''
    Build common data structurs with the built-in data types
'''


class Queue:
    '''
        Build a queue with the built-in list
    '''
    def __init__(self):
        self.q = []

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):
        return self.q.pop(0)

    def is_empty(self):
        return len(self.q) == 0

    def peek(self):
        return self.q[0]

    def size(self):
        return len(self.q)


class Stack:
    '''
        Build a stack with the built-in list
    '''
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