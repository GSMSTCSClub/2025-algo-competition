from os.path import join
import random
import sys
from time import perf_counter


FOLDER_PATH = "test-data"
TESTS: list[list | str] = [
    """\
3
10 3
1 9 5
5 8
1 2 3 4 5 6 7 8
6 4
99 65 45 21""",
    [1, 10, 10],
    [10, 10, 10],
    [100, 10, 10],
    [1, 100, 100],
    [10, 100, 100],
    [100, 100, 100],
    [1, 1000, 1000],
    [10, 1000, 1000],
    [100, 1000, 1000],
    [1, 10_000, 10_000],
    [10, 10_000, 10_000],
    [50, 10_000, 10_000],
    [1, 100_000, 100_000],
    [3, 90_000, 100_000],
    [3, 90_000, 100_000],
]
random.seed(0)


def solution():
    """Generates solution for a testcase. Expects input from std.in and expects output from std.out."""
    for _ in range(int(input())):
        T, _ = map(int, input().split())
        S = list(map(int, input().split()))
        sums_dic = {0: -1}
        sums_list = [0]
        
        for num in S:
            found = False
            for i in range(len(sums_list)):
                cur = sums_list[i] + num
                if cur == T:
                    ans = [num]
                    retrieve = sums_list[i]
                    while retrieve != 0:
                        ans.append(sums_dic[retrieve])
                        retrieve -= sums_dic[retrieve]
                    print(" ".join(map(str, ans)))
                    found = True
                    break
                elif cur < T and cur not in sums_dic:
                    sums_dic[cur] = num
                    sums_list.append(cur)
            if found:
                break
        else:
            print("IMPOSSIBLE")


def generate(*args):
    """Generates a test case. Expects an output from std.out."""
    if len(args) == 1 and type(args[0]) == str:
        print(args[0])  # just printout the pre-written testcase
        return
    T, t, n = args
    print(T)
    for _ in range(T):
        print(t, n)
        values = set()
        while len(values) < n:
            values.add(random.randint(1, 10 * n))
        print(" ".join(map(str, values)))


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
