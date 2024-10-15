'''
    calculate sum of 1 + 2 + 3 + ... + n
'''


def sum_recurrence(lt):
    ''' Calculate the sum of a list with recurrence '''
    s = 0
    for i in lt:
        s += i
    return s


def sum_recursion(lt, cur):
    ''' Calculate the sum of a list with recursion '''
    if cur == len(lt):
        return 0
    return lt[cur] + sum_recursion(lt, cur+1)


if __name__ == '__main__':
    test_lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_1 = sum_recurrence(test_lt)
    sum_2 = sum_recursion(test_lt, 0)

    print(f"{sum_1} and {sum_2} are equal.")
