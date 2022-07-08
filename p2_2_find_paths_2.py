'''
    find ways out of a maze 2
'''


from ds_tools import build_tree, Stack


def find_paths(node, stk, paths):
    stk.push(node)
    if not node.left and not node.right and not 21 % node.val:
        paths.append(list(stk))
    if node.left:
        find_paths(node.left, stk, paths)
    if node.right:
        find_paths(node.right, stk, paths)


if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(lt, 0, len(lt)-1)

    paths = []

    find_paths(root, [], paths)
    for path in paths:
        vals = [node.val for node in path]
        print(vals)
