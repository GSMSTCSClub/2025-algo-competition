from functools import reduce
for _ in range(int(input().strip()) ):
    N, I, A, M = map(int, input().strip().split(" "))
    D=max(0,N-A)
    adds = sorted(list(map(float, input().strip().split(" "))), reverse=True)[0:min(A, N)][::-1]
    muls = sorted(list(map(float, input().strip().split(" "))), reverse=True)
    a,m=I+sum(adds),reduce(lambda x,y:x*y, muls[0:D]) if D else 1
    
    mx=a*m
    print(a,m,mx)
    for s in range(min(N,A,M-D)):
        a-=adds[s]
        m*=muls[D+s]
        print(a,m, a*m)
        mx =max(mx, a*m)
    print(int(mx))