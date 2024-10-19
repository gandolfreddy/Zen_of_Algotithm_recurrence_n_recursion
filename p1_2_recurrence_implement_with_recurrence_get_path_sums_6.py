'''
    Get path sums 6 by simulating recursion with stack
'''


from ds_tools import Node, Stack


class Frame:
    ''' Frame for simulating recursion '''

    def __init__(self, node):
        self.node = node
        self.cnt = 0
        self.sums = []


def add_child(node, val, to_left):
    ''' Add a child to a node '''
    child = Node(val)
    if to_left:
        node.left = child
    else:
        node.right = child
    return child


def build_tree(n):
    ''' Build a binary tree with n levels '''
    root = Node(1)
    p, q = root, root

    for _ in range(1, n+1):
        p = add_child(p, 1, True)
        q = add_child(q, 1, False)

    pp, qq = p, q
    for _ in range(1, n+1):
        p = add_child(p, 1, True)
        pp = add_child(pp, 1, False)

        q = add_child(q, 1, False)
        qq = add_child(qq, 1, True)

    return root


def get_path_sums(root):
    ''' Get the path sums of a binary tree '''
    stk = Stack()
    primer = Frame(root)
    stk.push(primer)

    while True:
        top = stk.peek()
        if top.node is None:
            stk.pop()
            # 上一層 Frame 的 cnt 加 1
            stk.peek().cnt += 1
        elif top.cnt == 0:
            stk.push(Frame(top.node.left))
        elif top.cnt == 1:
            stk.push(Frame(top.node.right))
        else:
            popped = stk.pop()
            if not popped.sums:
                popped.sums.append(popped.node.val)
            if stk.is_empty():
                break
            top = stk.peek()
            for s in popped.sums:
                top.sums.append(s + top.node.val)
            top.cnt += 1

    return primer.sums


if __name__ == "__main__":
    test_root = build_tree(20000)
    test_sums = get_path_sums(test_root)
    print(test_sums)
