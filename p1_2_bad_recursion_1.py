'''
    Bad recursion test 1
'''


def go_deeper(level):
    ''' Go deeper '''
    # side condition
    # if level == 10000: return
    print(level)
    go_deeper(level + 1)


if __name__ == "__main__":
    go_deeper(0)
    # eventually the program will stack overflow
    # because the stack is too deep (level 995)
    # and the program will not finish
