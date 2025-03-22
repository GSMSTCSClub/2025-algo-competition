import random
import sys
from time import perf_counter


INPUT_FILE_PATH = ""
OUTPUT_FOLDER_PATH = ""
TESTS: list[list | str] = [
    [],  # configs for the inputs should be set here. Should be a list
    "",  # a full test can also be placed here as needed, this can be used to test weird edge cases 
         # or for the test inputs. Should of a string.
]
random.seed(0)


def solution():
    """Generates solution for a testcase. Expects input from std.in and expects output from std.out."""
    ...


def generate(*args):
    """Generates a test case. Expects an output from std.out."""
    if len(args) == 1 and type(args[0]) == str:
        print(args[0])  # just printout the pre-written testcase
    ...


def main():
    for test_num, test in enumerate(TESTS):
        with open(INPUT_FILE_PATH, mode='w') as sys.stdout:
            generate(*test)
        start_time = perf_counter()
        with open(OUTPUT_FOLDER_PATH + f"{test_num}.txt", mode='w') as sys.stdout:
            with open(INPUT_FILE_PATH) as sys.stdin:
                solution()
        end_time = perf_counter()
        assert end_time - start_time < 10, "It should not take more than 10s to solve the testcase."


if __name__ == "__main__":
    main()
