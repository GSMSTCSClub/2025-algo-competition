I=input
L=int
M=map
P=print
R=range
for _ in R(L(I())):
 T,_=M(L,I().split())
 S=list(M(L,I().split()))
 d={0:-1}
 l=[0]
 for n in S:
  f=False
  for i in R(len(l)):
   c=l[i]+n
   if c==T:
    a=[n]
    r=l[i]
    while r!=0:a.append(d[r]);r-=d[r]
    P(" ".join(M(str,a)))
    f=True
    break
   elif c<T and c not in d:d[c]=n;l.append(c)
  if f:break
 else:P("IMPOSSIBLE")