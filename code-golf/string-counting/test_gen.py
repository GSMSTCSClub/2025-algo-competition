from os.path import join
import random
import sys
from time import perf_counter


FOLDER_PATH = "test-data"
TESTS: list[list | str] = [
    """\
3
hello helloworldhello
testing testsarecool
aa aaaaaaaa""",
    [1, 2, 1000],
    [10, 2, 1000],
    [100, 2, 1000],
    [1, 10, 10_000],
    [10, 10, 10_000],
    [100, 10, 10_000],
    [1, 10, 100_000],
    [10, 10, 100_000],
    [100, 10, 100_000],
    [100, 10, 100_000],
]
random.seed(0)


def solution():
    """Generates solution for a testcase. Expects input from std.in and expects output from std.out."""
    for _ in range(int(input())):
        s1, s2 = input().split()
        print(sum(s1 == s2[i:i + len(s1)] for i in range(len(s2) - len(s1) + 1)))


def generate(*args):
    """Generates a test case. Expects an output from std.out."""
    if len(args) == 1 and type(args[0]) == str:
        print(args[0])  # just printout the pre-written testcase
        return
    t, l1, l2 = args
    char_set = "qwertyuiopasdfghjklzxcvbnm" if l2 == 1000 else "ab"
    print(t)
    for _ in range(t):
        print("".join(random.choices(char_set, k=l1)), "".join(random.choices(char_set, k=l2)))


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
