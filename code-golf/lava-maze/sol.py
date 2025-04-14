I=input
D=[(-1,0),(1,0),(0,-1),(0,1)]
def e(g,n):
 q=[(0,0)]
 while q:
  x,y=q.pop()
  if not g[x][y]:continue
  g[x][y]=False
  if x==n-1 and y==n-1: return 1
  for i,j in D:
   nx,ny=x+i,y+j
   if 0<=nx<n and 0<=ny<n and g[nx][ny]:q.append((nx, ny))
 return 0
n=int(I())
G=[list(map(int,I().split()))for _ in range(n)]
l,r=min(min(r)for r in G),max(max(r)for r in G)
v=0
while l<=r:
 m=(l+r)//2
 g=[[val>=m for val in row]for row in G]
 if e(g,n):v=m;l=m+1
 else:r=m-1
print(v)