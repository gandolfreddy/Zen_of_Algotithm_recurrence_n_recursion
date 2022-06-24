'''
    Bad recursion test 3 with sum example
'''


def sum_recurrence(lt):
    s = 0
    for i in lt: s += i
    return s


def sum_recursion(lt, cur):
    if cur == len(lt): return 0
    return lt[cur] + sum_recursion(lt, cur+1)


if __name__ == '__main__':
    lt = [1 for _ in range(25000)]

    sum1 = sum_recurrence(lt)
    print(f"sum1: {sum1}")
    sum2 = sum_recursion(lt, 0)
    print(f"sum1: {sum2}")
    