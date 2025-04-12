from os.path import join
import random
import sys
from time import perf_counter

maxW=1024
maxE=1024
maxN=1024
maxR=1
FOLDER_PATH = "code-golf/0.5-f2p/test-data"
TESTS: list[list | str] = [
"""\
2
60
3
0:0.6
40:1.2
90:100
60
2
0:1
40:2
""",  
[1,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],
[2,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],
[3,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],
[4,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],
[5,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],
[6,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],
[7,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],
[8,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],
[9,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],
[10,random.randint(1,maxW),random.randint(1,maxE),(random.random()*maxR)**4],

]
random.seed(0)


def solution():
    """Generates solution for a testcase. Expects input from std.in and expects output from std.out."""
    for _ in range(int(input().strip())):
        W = int(input().strip())
        E = int(input().strip())
        D = tuple(tuple(map(float, input().split(":"))) for i in range(E))
        #Losingrate[xWishes] = (1-winRate)^xWishes
        TotalloseRate=1
        i=0
        while i+1 < len(D) and D[i+1][0] < W:
            threshold, rate = D[i]
            # print(threshold, TotalloseRate)
            TotalloseRate*=(1-rate/100)**(D[i+1][0]-threshold)
            i+=1
        TotalloseRate*=(1-D[i][1]/100)**(W-D[i][0])
                
        # print( TotalloseRate)
        print( TotalloseRate<0.5 )

def generate(*args):
    """Generates a test case. Expects an output from std.out."""
    if len(args) == 1 and type(args[0]) == str:
        print(args[0])  # just printout the pre-written testcase
        return
    T,W,E,baseRate=args
    print(T)
    for _ in range(T):
        print(W)
        print(E)
        print(f"0:{baseRate}")
        B=baseRate
        Zone = 0
        ZoneIncrement = [random.randint(1,max(1,W*4//E)) for i in range(E-1)]
        for i in range(E-1):
            Zone+=ZoneIncrement.pop(0)
            B=B+random.random()*B
            print(f"{Zone}:{B*100}")
            


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
