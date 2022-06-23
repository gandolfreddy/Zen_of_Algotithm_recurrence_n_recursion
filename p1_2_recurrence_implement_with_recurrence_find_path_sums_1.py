'''
    Find path sums 1
'''


from p1_2_prepare_a_binary_tree import build_tree


def get_path_sums(root):
    sums = list()
    sum_q = list()
    node_q = list()
    
    sum_q.append(0)
    node_q.append(root)

    while node_q:
        cur_node = node_q.pop(0)
        if cur_node == None: continue
        cur_sum = cur_node.val + sum_q.pop(0)
        if cur_node.left == None and cur_node.right == None:
            sums.append(cur_sum)
        sum_q.append(cur_sum)
        node_q.append(cur_node.left)
        sum_q.append(cur_sum)
        node_q.append(cur_node.right)
    
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
        
    sums = get_path_sums(root)
    print(sums)
