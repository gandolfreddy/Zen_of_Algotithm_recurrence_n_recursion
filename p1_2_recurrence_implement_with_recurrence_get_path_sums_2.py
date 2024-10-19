'''
    Get path sums 2
'''


from ds_tools import build_tree


def get_path_sums(root):
    ''' Get the path sums of a binary tree '''
    sums = {}
    node_q = []

    sums[root] = root.val
    node_q.append(root)

    while node_q:
        cur_node = node_q.pop(0)
        cur_sum = sums[cur_node]

        # 去除不完全路徑和
        # if cur_node.left != None or cur_node.right != None:
        #     sums.pop(cur_node)

        if cur_node.left is not None:
            node_q.append(cur_node.left)
            sums[cur_node.left] = cur_sum + cur_node.left.val

        if cur_node.right is not None:
            node_q.append(cur_node.right)
            sums[cur_node.right] = cur_sum + cur_node.right.val

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

    test_sums = get_path_sums(test_root)
    for k, v in test_sums.items():
        print(f"Road to {k.val}: {v}")
