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