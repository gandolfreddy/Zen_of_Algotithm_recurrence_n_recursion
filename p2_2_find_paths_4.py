'''
    find ways out of a maze 4
'''


from ds_tools import build_tree, Stack


def find_paths(root):
    paths = []
    cnts = {}
    path = Stack()

    cnts[root] = 0
    path.push(root)

    while True:
        top = path.peek()
        if cnts.get(top) == 0:
            if not top.left:
                cnts[top] = 1
            else:
                path.push(top.left)
                cnts[top.left] = 0
        elif cnts.get(top) == 1:
            if not top.right:
                cnts[top] = 2
            else:
                path.push(top.right)
                cnts[top.right] = 0
        elif cnts.get(top) == 2:
            if not top.left and not top.right and not 21 % top.val:
                paths.append(list(path))
            path.pop()
            if path.is_empty(): break
            top = path.peek()
            cnts[top] += 1
    
    return paths


if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(lt, 0, len(lt)-1)

    paths = find_paths(root)
    for path in paths:
        vals = [node.val for node in path]
        print(vals)
