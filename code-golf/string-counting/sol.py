I=input
R=range
L=len
for _ in R(int(I())):
 s1,s2=I().split()
 print(sum(s1==s2[i:i+L(s1)] for i in R(L(s2)-L(s1)+1)))