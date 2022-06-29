'''
    Get path sums 6 by simulating recursion with stack
'''


from p1_2_prepare_a_binary_tree import Node


class Frame:
    def __init__(self, node):
        self.node = node
        self.cnt = 0
        self.sums = []


def add_child(node, val, to_left):
    child = Node(val)
    if to_left:
        node.left = child
    else:
        node.right = child
    return child


def build_tree(n):
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
    stk = []
    primer = Frame(root)
    stk.append(primer)

    while True:
        top = stk[-1]
        if top.node is None:
            stk.pop()
            stk[-1].cnt += 1
        elif top.cnt == 0:
            stk.append(Frame(top.node.left))
        elif top.cnt == 1:
            stk.append(Frame(top.node.right))
        else:
            popped = stk.pop()
            if not popped.sums:
                popped.sums.append(popped.node.val)
            if not stk: break
            top = stk[-1]
            for s in popped.sums:
                top.sums.append(s + top.node.val)
            top.cnt += 1
    
    return primer.sums


if __name__ == "__main__":
    root = build_tree(20000)
    sums = get_path_sums(root)
    print(sums)

