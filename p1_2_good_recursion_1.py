'''
    Good recursion 1: tail-recursion
    However, Python does not support a tail-recursion optimization.
    see: 
        1. http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html
        2. https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion
'''

s = 0


def sum_next(lt, i):
    global s

    if i == len(lt): return 0
    s += lt[i]
    sum_next(lt, i+1)


if __name__ == "__main__":
    lt = [1 for _ in range(250000)]
    sum_next(lt, 0)
    print(s)
