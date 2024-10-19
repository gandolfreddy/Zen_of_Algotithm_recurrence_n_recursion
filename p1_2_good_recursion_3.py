'''
    Good recursion 3: with divide and conquer (binary) technique
'''


def sum_next(lt, li, hi):
    ''' Sum with recursion '''
    if li > hi:
        return 0
    mi = li + (hi - li) // 2
    return sum_next(lt, li, mi-1) + lt[mi] + sum_next(lt, mi+1, hi)


if __name__ == "__main__":
    test_lt = [1 for _ in range(250000)]
    s = sum_next(test_lt, 0, len(test_lt)-1)
    print(s)
