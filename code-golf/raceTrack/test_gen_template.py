from os.path import join
import random
import sys
from time import perf_counter

maxW=100
maxL=100
FOLDER_PATH = "code-golf/raceTrack/test-data"
TESTS: list[list | str] = [
"""\
1
3 5
000
110
010
010
011
""",  
[1,random.randint(1,maxW),random.randint(1,maxL)],
[2,random.randint(1,maxW),random.randint(1,maxL)],
[3,random.randint(1,maxW),random.randint(1,maxL)],
[4,random.randint(1,maxW),random.randint(1,maxL)],
[5,random.randint(1,maxW),random.randint(1,maxL)],
[6,random.randint(1,maxW),random.randint(1,maxL)],
[7,random.randint(1,maxW),random.randint(1,maxL)],
[8,random.randint(1,maxW),random.randint(1,maxL)],
[9,random.randint(1,maxW),random.randint(1,maxL)],
[10,random.randint(1,maxW),random.randint(1,maxL)],

]
random.seed(0)


def solution():
    """Generates solution for a testcase. Expects input from std.in and expects output from std.out."""
    def ans(rows, pv, w, l):
        for i in range(1,l):
            row = [1] * w
            for j in range(w):
                if (pv[j]==rows[i][j] and pv[j]==0) or ((j-1 >=0) and row[j-1] == 0 and rows[i][j] == 0):
                    row[j] = 0
            for j in range(w-2,-1,-1):
                if row[j+1] == 0 and rows[i][j] == 0:
                    row[j] = 0
            pv=row
            # print(">",row)
        return 0 in pv
    for _ in range(int(input().strip()) ):
        w,l = map(int, input().strip().split(" "))
        rows = [list(int(i) for i in input().strip()) for i in range(l)]
        pv=rows[0]
        # print("pv", pv)
        print(ans(rows,pv, w, l))


def generate(*args):
    """Generates a test case. Expects an output from std.out."""
    if len(args) == 1 and type(args[0]) == str:
        print(args[0])  # just printout the pre-written testcase
        return
    T,W,H=args
    print(T)
    for _ in range(T):
        print(W,H)
        for i in range(H):
            print("".join(str(0 if random.random() > (random.random()*0.5+0.125) else 1) for j in range(W)))


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
