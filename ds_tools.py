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


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(lt, li, hi):
    if li > hi: return None
    mid = li + (hi - li) // 2
    root = Node(lt[mid])
    root.left = build_tree(lt, li, mid-1)
    root.right = build_tree(lt, mid+1, hi)
    return root