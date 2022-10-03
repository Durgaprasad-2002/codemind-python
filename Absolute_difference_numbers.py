import math
def fd(n,m):
    l=len(str(n))
    p=int(math.pow(10,l-m))
    return (int(n/p))
def ld(n,m):
    p=int(math.pow(10,m))
    return n%p
n,m=map(int,input().split())
firstd=fd(n,m)
lastd=ld(n,m)
s=firstd-lastd
if s<0:
    print(s//-1)
else:
    print(s)
    
    