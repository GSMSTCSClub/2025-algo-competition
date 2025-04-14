R=range
S=sorted
L=len
I=input
def w(s):
 n=L(s)
 y=S(R(n),key=lambda i:s[i])
 r=[0]*n
 q=lambda i:(r[i],r[i+k]if i+k<n else -1)
 for i in R(1,n): 
  c,p=y[i],y[i-1]
  r[c]=r[p]+(s[c]!=s[p])
 k=1
 while k<n:
  y=S(y,key=q)
  u=[0]*n
  for i in R(1,n):
   c,p=y[i],y[i-1]
   u[c]=u[p]+(q(p)!=q(c))
  r=u
  k*=2
 return y
def h(s,y):
 n = L(s)
 l = [0]*n
 r = [0]*n
 for i in R(n):r[y[i]]=i
 k=0
 for i in R(n):
  if r[i]==n-1:k=0;continue
  j=y[r[i]+1]
  while i+k<n and j+k<n and s[i+k]==s[j+k]:k+=1
  l[r[i]]=k
  if k>0:k-=1
 return l
def lcs(e,r):
 s=e+'#'+r
 n=L(s)
 q=L(e)
 f=w(s)
 l=h(s, f)
 return max(l[i-1]for i in R(1,n)if(f[i]<q)^(f[i-1]<q))
j,n,l,t=map(int,I().split())
g=[I()for _ in R(t)]
c={}
for _ in R(j):z=I();c[z]=[I()for _ in R(n)]
print(" ".join(x for _,x in sorted([-sum(max(lcs(v,b)for b in g)for v in a),d]for d, a in c.items())))