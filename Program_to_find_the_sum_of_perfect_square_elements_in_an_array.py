from math import sqrt
n=int(input())
d=list(map(int,input().split()))
def perfect(n):
    m=sqrt(n)
    if m-int(m)>0:
        return False
    else:
        return True
s=0
for i in d:
    if perfect(i):
        s+=i
print(s)