'''
    Get path sums 4 with collect_sums()
'''


from p1_2_prepare_a_binary_tree import build_tree


def collect_sums(root):
    sums = list()
    if not root: return sums
    sums += collect_sums(root.left)
    sums += collect_sums(root.right)
    for i in range(len(sums)):
        sums[i] += root.val
    if not sums: sums.append(root.val)
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
    
    sums = collect_sums(root)
    print(sums)

