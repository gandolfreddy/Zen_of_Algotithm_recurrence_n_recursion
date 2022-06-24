'''
    Get path sums 3
'''


from p1_2_prepare_a_binary_tree import build_tree


def get_path_sums(root, parent_sum, sums):
    if not root: return 
    cur_sum = parent_sum + root.val
    if not root.left and not root.right:
        sums.append((root.val, cur_sum))
    ## 將「半成品」結果向左下傳遞
    get_path_sums(root.left, cur_sum, sums)
    ## 將「半成品」結果向右下傳遞
    get_path_sums(root.right, cur_sum, sums)


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
    
    sums = list()
    get_path_sums(root, 0, sums)
    print(sums)

