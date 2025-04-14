from os.path import join
import random
import sys
from time import perf_counter


FOLDER_PATH = "test-data"
TESTS: list[list | str] = [
    """\
10
9 5 3 2 4 6 8 4 2 5
8 7 6 4 1 5 2 4 8 4
6 3 8 9 4 2 1 5 8 4
8 6 2 4 7 9 9 3 2 1
4 5 9 5 6 7 8 2 1 3
1 2 3 2 5 4 8 5 4 8
4 6 3 2 7 8 5 4 9 1
1 5 7 6 3 4 8 2 5 9
5 6 3 4 2 1 8 2 7 6
4 5 6 4 2 3 7 9 5 9""",
    [10, 1e9],
    [20, 10],
    [20, 1e9],
    [50, 1e5],
    [50, 1e9],
    [100, 1e5],
    [100, 1e9],
    [200, 1e5],
    [200, 1e9],
    [400, 1e5],
    [400, 1e9],
    [800, 1e5],
    [800, 1e9],
    [1000, 1e5],
    [900, 1e9],
]
random.seed(0)


def solution():
    """Generates solution for a testcase. Expects input from std.in and expects output from std.out."""
    from collections import deque
    DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def can_escape():
        to_visit = deque()
        to_visit.append((0, 0))
        while to_visit:
            loc = to_visit.pop()
            if not ngrid[loc[0]][loc[1]]: continue
            ngrid[loc[0]][loc[1]] = False
            if loc == (n - 1, n - 1): return True
            for dx, dy in DIRS: 
                nx, ny = loc[0] + dx, loc[1] + dy
                if 0 <= nx < n and 0 <= ny < n:
                    to_visit.append((nx, ny))
        return False
    n = int(input())
    grid = []
    for _ in range(n): grid.append(list(map(int, input().split())))
    l, r = grid[0][0], grid[0][0]
    for row in grid:
        for v in row:
            l = min(l, v)
            r = max(r, v)
    max_v = 0
    while l <= r:
        m = (l + r) // 2
        ngrid = []
        for i in range(len(grid)): ngrid.append([v >= m for v in grid[i]])
        if can_escape():
            max_v = max(max_v, m)
            l = m + 1
        else:
            r = m - 1
    print(max_v)


def generate(*args):
    """Generates a test case. Expects an output from std.out."""
    if len(args) == 1 and type(args[0]) == str:
        print(args[0])  # just printout the pre-written testcase
        return
    N, M = args
    print(N)
    for _ in range(N):
        print(" ".join(map(str, [random.randint(1, int(M)) for _ in range(N)])))
    


def main():
    for test_num, test in enumerate(TESTS):
        input_path = join(FOLDER_PATH, f"{test_num}in.txt")
        output_path = join(FOLDER_PATH, f"{test_num}out.txt")
        with open(input_path, mode='w') as sys.stdout:
            if isinstance(test, str):
                generate(test)
            else:
                generate(*test)
        start_time = perf_counter()
        with open(output_path, mode='w') as sys.stdout:
            with open(input_path) as sys.stdin:
                solution()
        end_time = perf_counter()
        assert end_time - start_time < 10, "It should not take more than 10s to solve the testcase."


if __name__ == "__main__":
    main()
