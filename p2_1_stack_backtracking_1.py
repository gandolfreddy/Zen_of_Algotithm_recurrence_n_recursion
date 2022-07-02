'''
    understand backtracking with stack
'''


from ds_tools import Stack


def action(n, max_n, stk):
    stk.push(n)
    print(f"Pushed\t{n}")
    if n < max_n: action(n+1, max_n, stk)
    stk.pop()
    print(f"Popped\t{n}")


def stack_backtracking():
    stk = Stack()
    print(f"Stack size: {stk.size()}")
    print("============")
    action(98, 100, stk)
    print("============")
    print(f"Stack size: {stk.size()}")


if __name__ == '__main__':
    stack_backtracking()
