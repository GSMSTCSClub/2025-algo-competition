"""
1
3 5
000
110
010
000
011
"""
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