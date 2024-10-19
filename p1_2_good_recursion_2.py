'''
    Good recursion 2: with divide and conquer (binary) technique
'''


def sum_next(lt, li, hi):
    ''' Sum with recursion '''
    if li == hi:
        return lt[li]
    mi = li + (hi - li) // 2
    return sum_next(lt, li, mi) + sum_next(lt, mi+1, hi)


if __name__ == "__main__":
    test_lt = [1 for _ in range(250000)]
    s = sum_next(test_lt, 0, len(test_lt)-1)
    print(s)
