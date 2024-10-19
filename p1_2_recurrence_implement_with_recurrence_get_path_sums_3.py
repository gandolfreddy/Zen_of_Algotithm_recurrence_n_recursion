'''
    Get path sums 3
'''


from ds_tools import build_tree


def get_path_sums(root, parent_sum, sums):
    ''' Get the path sums of a binary tree '''
    if not root:
        return
    cur_sum = parent_sum + root.val
    if not root.left and not root.right:
        sums.append((root.val, cur_sum))
    # 將「半成品」結果向左下傳遞
    get_path_sums(root.left, cur_sum, sums)
    # 將「半成品」結果向右下傳遞
    get_path_sums(root.right, cur_sum, sums)


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

    test_sums = list()
    get_path_sums(test_root, 0, test_sums)
    print(test_sums)
