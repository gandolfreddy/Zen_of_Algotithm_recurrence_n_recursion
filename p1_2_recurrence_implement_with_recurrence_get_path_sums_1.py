'''
    Get path sums 1
'''


from ds_tools import build_tree


def get_path_sums(root):
    ''' Get the path sums of a binary tree '''
    sums = []
    sum_q = []
    node_q = []

    sum_q.append(0)
    node_q.append(root)

    while node_q:
        cur_node = node_q.pop(0)
        if cur_node is None:
            continue
        cur_sum = cur_node.val + sum_q.pop(0)
        if cur_node.left is None and cur_node.right is None:
            sums.append(cur_sum)
        sum_q.append(cur_sum)
        node_q.append(cur_node.left)
        sum_q.append(cur_sum)
        node_q.append(cur_node.right)

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

    test_sums = get_path_sums(test_root)
    print(test_sums)
