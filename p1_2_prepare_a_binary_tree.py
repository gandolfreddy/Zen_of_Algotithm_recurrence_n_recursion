'''
    Prepare a binary tree from a sorted list.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(lt, li, hi):
    if li > hi: return None
    mid = li + (hi - li) // 2
    root = Node(lt[mid])
    root.left = build_tree(lt, li, mid-1)
    root.right = build_tree(lt, mid+1, hi)
    return root


if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(lt, 0, len(lt)-1)
    