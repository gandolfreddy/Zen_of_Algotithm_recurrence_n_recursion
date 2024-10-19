'''
    Bad recursion test 3 with sum example
'''


def sum_recurrence(lt):
    ''' Sum with recurrence '''
    s = 0
    for i in lt:
        s += i
    return s


def sum_recursion(lt, cur):
    ''' Sum with recursion '''
    if cur == len(lt):
        return 0
    return lt[cur] + sum_recursion(lt, cur+1)


if __name__ == '__main__':
    test_lt = [1 for _ in range(25000)]

    sum1 = sum_recurrence(test_lt)
    print(f"sum1: {sum1}")
    sum2 = sum_recursion(test_lt, 0)
    print(f"sum1: {sum2}")
