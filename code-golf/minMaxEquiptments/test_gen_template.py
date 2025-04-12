from os.path import join
import random
import sys
from time import perf_counter

CeilN = 64
CeilI = 64
CeilA = 64
CeilM = 8
CeilAdd = 64
CeilMul = 8

FOLDER_PATH = "test-data"
TESTS: list[list | str] = [ 
"""\
2
4 100 3 3
100 200 150 
2 1.5 1.2
5 0 5 5
1 1 1 1 1
1.1 1.1 1.1 1.1 2.1
""",
[random.randint(0,CeilN),random.randint(0,CeilI),random.randint(0,CeilA),random.randint(0,CeilM)],
[random.randint(0,CeilN),random.randint(0,CeilI),random.randint(0,CeilA),random.randint(0,CeilM)],
[random.randint(0,CeilN),random.randint(0,CeilI),random.randint(0,CeilA),random.randint(0,CeilM)],
[random.randint(0,CeilN),random.randint(0,CeilI),random.randint(0,CeilA),random.randint(0,CeilM)],
[random.randint(0,CeilN),random.randint(0,CeilI),random.randint(0,CeilA),random.randint(0,CeilM)],
[random.randint(0,CeilN),random.randint(0,CeilI),random.randint(0,CeilA),random.randint(0,CeilM)],
[random.randint(0,CeilN),random.randint(0,CeilI),random.randint(0,CeilA),random.randint(0,CeilM)],
[random.randint(0,CeilN),random.randint(0,CeilI),random.randint(0,CeilA),random.randint(0,CeilM)],
]
random.seed(0)


def solution():
    """Generates solution for a testcase. Expects input from std.in and expects output from std.out."""
    
    from functools import reduce
    for _ in range(int(input().strip()) ):
        N, I, A, M = map(int, input().strip().split(" "))
        N=min(N, A+M)
        D=max(0,N-A)
        adds = sorted(list(map(float, input().strip().split(" "))), reverse=True)[0:min(A, N)][::-1] if A else [0]
        muls = sorted(list(map(float, input().strip().split(" "))), reverse=True) if M else [1]
        a,m=I+sum(adds),reduce(lambda x,y:x*y, muls[0:D]) if D else 1
        
        mx=a*m
        # print(a,m,mx)
        for s in range(min(N,A,M-D)):
            a-=adds[s]
            m*=muls[D+s]
            mx =max(mx, a*m)
        print(int(mx))

def generate(*args):
    """Generates a test case. Expects an output from std.out."""
    if len(args) == 1 and type(args[0]) == str:
        print(args[0])  # just printout the pre-written testcase
        return
    print(1)  
    
    N, I, A, M = args
    
    print(N, I, A, M)
    print(" ".join(str(random.randint(0,CeilAdd)) for i in range(A)))
    print(" ".join(str(random.random() * (CeilMul-1)+1) for i in range(M))) 


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
