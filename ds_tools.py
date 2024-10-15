'''
    Build common data structurs with the built-in data types
'''


class Queue:
    '''
        Build a queue with the built-in list
    '''

    def __init__(self):
        self.q = []
        self.current_size = 0

    def enqueue(self, val):
        ''' Add an element to the end of the queue '''
        self.q.append(val)
        self.current_size += 1

    def dequeue(self):
        ''' Remove an element from the front of the queue '''
        if self.is_empty():
            return None
        self.current_size -= 1
        return self.q.pop(0)

    def is_empty(self):
        ''' Check if the queue is empty '''
        return self.current_size == 0

    def peek(self):
        ''' Get the element at the front of the queue '''
        return self.q[0]

    def size(self):
        ''' Get the size of the queue '''
        return self.current_size


class Stack:
    '''
        Build a stack with the built-in list
    '''

    def __init__(self):
        self.stk = []
        self.current_size = 0

    def push(self, val):
        ''' Add an element to the top of the stack '''
        self.stk.append(val)
        self.current_size += 1

    def pop(self):
        ''' Remove an element from the top of the stack '''
        if self.is_empty():
            return None
        self.current_size -= 1
        return self.stk.pop()

    def is_empty(self):
        ''' Check if the stack is empty '''
        return self.current_size == 0

    def peek(self):
        ''' Get the element at the top of the stack '''
        return self.stk[-1]

    def size(self):
        ''' Get the size of the stack '''
        return self.current_size

    def __iter__(self):
        return (elem for elem in self.stk)


class Node:
    '''
        Build a binary tree node
    '''

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(lt, li, hi):
    ''' Build a binary search tree from a sorted list '''
    if li > hi:
        return None
    mid = li + (hi - li) // 2
    root = Node(lt[mid])
    root.left = build_tree(lt, li, mid-1)
    root.right = build_tree(lt, mid+1, hi)
    return root
