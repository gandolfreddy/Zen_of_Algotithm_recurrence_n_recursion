'''
    Prepare a binary tree from a sorted list.
'''

from ds_tools import build_tree

if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(lt, 0, len(lt)-1)
