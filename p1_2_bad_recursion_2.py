'''
    Bad recursion test 2 with try-except
'''


def go_deeper(level):
    ''' Go deeper '''
    # side condition
    # if level == 10000: return
    print(level)
    try:
        go_deeper(level + 1)
    except:
        print("stack overflow")
        return


if __name__ == "__main__":
    try:
        go_deeper(0)
    except:
        print("stack overflow")

    # eventually the program will stack overflow
    # in Python, try-except works unlike in Java
