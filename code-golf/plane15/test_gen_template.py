from os.path import join
import random
import sys
from time import perf_counter

maxX=1024
maxY=1024
FOLDER_PATH = "test-data"
TESTS: list[list | str] = [
"""\
8 0
4 0
""",  
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
[(1-random.random())*maxX,(1-random.random())*maxY,(1-random.random())*maxX,(1-random.random())*maxY,],
]
random.seed(0)


def solution():
    """Generates solution for a testcase. Expects input from std.in and expects output from std.out."""
    x,y = map(float,input().split(" "))
    a,b = map(float,input().split(" "))
    print( (x**2+y**2)<=(a**2+b**2) )


def generate(*args):
    """Generates a test case. Expects an output from std.out."""
    if len(args) == 1 and type(args[0]) == str:
        print(args[0])  # just printout the pre-written testcase
        return
    X,Y,A,B=args
    print(X,Y)
    print(A,B)


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
