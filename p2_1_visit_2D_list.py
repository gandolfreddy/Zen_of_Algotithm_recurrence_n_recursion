'''
    visit a 2D list with bracktracking skill
'''


def visit(visited: list[list], n: int):
    h, w = len(visited), len(visited[0])
    if n == h * w: return
    r, c = n // w, n % w
    visited[r][c] = True
    print(f"Visited ({r}, {c})")
    visit(visited, n+1)
    visited[r][c] = False
    print(f"Unvisited ({r}, {c})")


def count_visited(m: list[list]):
    cnt = 0
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c]: cnt += 1
    return cnt


if __name__ == "__main__":
    visited = [[False for __ in range(3)] for _ in range(2)]
    print(f"Visited: {count_visited(visited)}")
    print("============")
    visit(visited, 0)
    print("============")
    print(f"Visited: {count_visited(visited)}")
