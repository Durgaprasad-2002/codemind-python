from math import pow
a,b,c=map(int,input().split())
s1=pow(a,b)
r=s1%c
print(int(r))