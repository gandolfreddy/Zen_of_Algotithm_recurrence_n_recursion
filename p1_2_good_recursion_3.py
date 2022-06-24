'''
    Good recursion 3: with divide and conquer (binary) technique
'''


def sum_next(lt, li, hi):
    if li > hi: return 0
    mi = li + (hi - li) // 2
    return  sum_next(lt, li, mi-1) + lt[mi] + sum_next(lt, mi+1, hi)


if __name__ == "__main__":
    lt = [1 for _ in range(250000)]
    s = sum_next(lt, 0, len(lt)-1)
    print(s)
