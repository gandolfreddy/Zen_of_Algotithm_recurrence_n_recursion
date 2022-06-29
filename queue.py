'''
    Build a queue with the built-in list
'''


class Queue:
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