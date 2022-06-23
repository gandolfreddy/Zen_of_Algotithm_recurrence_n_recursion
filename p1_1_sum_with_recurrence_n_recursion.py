'''
    calculate sum of 1 + 2 + 3 + ... + n
'''


def sum_recurrence(lt):
    s = 0
    for i in lt: s += i
    return s


def sum_recursion(lt, cur):
    if cur == len(lt): return 0
    return lt[cur] + sum_recursion(lt, cur+1)


if __name__ == '__main__':
    lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum1 = sum_recurrence(lt)
    sum2 = sum_recursion(lt, 0)

    print(f"{sum1} and {sum2} are equal.")