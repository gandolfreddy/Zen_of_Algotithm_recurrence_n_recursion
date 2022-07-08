'''
    find ways out of a maze
'''


from logging import root
from ds_tools import Node, build_tree


def find_paths(node: Node, path: list[Node], paths: list[list[Node]]):
    path.append(node)
    if not node.left and node.right and not 21 % node.val:
        paths.append(path)
    if node.left:
        find_paths(node.left, [path], paths)
    if node.right:
        find_paths(node.right, [path], paths)


if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(lt, 0, len(lt)-1)
    paths = list(list())

    find_paths(root, [], paths)
    for path in paths:
        vals = [node.val for node in path]
        print(vals)
        