'''
    Get path sums 2
'''


from p1_2_prepare_a_binary_tree import build_tree


def get_path_sums(root):
    sums = dict()
    node_q = list()

    sums[root] = root.val
    node_q.append(root)

    while node_q:
        cur_node = node_q.pop(0)
        cur_sum = sums[cur_node]

        ## 去除不完全路徑和
        # if cur_node.left != None or cur_node.right != None:
        #     sums.pop(cur_node)

        if cur_node.left != None:
            node_q.append(cur_node.left)
            sums[cur_node.left] = cur_sum + cur_node.left.val

        if cur_node.right != None:
            node_q.append(cur_node.right)
            sums[cur_node.right] = cur_sum + cur_node.right.val

    return sums


if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(lt, 0, len(lt)-1)

    ## Binary Tree
    ##        4
    ##      /   \
    ##     2     6
    ##    / \   / \
    ##   1   3 5   7

    ## print the tree
    def print_tree(root):
        if root == None: return
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)

    print_tree(root)
    print()
        
    sums = get_path_sums(root)
    for k, v in sums.items():
        print(f"Road to {k.val}: {v}")

