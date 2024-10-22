'''
    Get path sums 4 with collect_sums()
'''


from ds_tools import build_tree


def collect_sums(root):
    ''' Collect the path sums of a binary tree '''
    sums = []
    if not root:
        return sums
    sums += collect_sums(root.left)
    sums += collect_sums(root.right)
    sums = [s + root.val for s in sums]
    if not sums:
        sums.append(root.val)
    return sums


if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5, 6, 7]
    test_root = build_tree(lt, 0, len(lt)-1)

    # Binary Tree
    #      4
    #    /   \
    #   2     6
    #  / \   / \
    # 1   3 5   7

    # print the tree
    def print_tree(root):
        ''' Print the binary tree '''
        if root is None:
            return
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)

    print_tree(test_root)
    print()

    test_sums = collect_sums(test_root)
    print(test_sums)
