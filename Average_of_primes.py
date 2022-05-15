from math import*
def prime(n):
    sq=int(sqrt(n))
    if n==1:
        return False
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
d=list(map(int,input().split()))
c=0
h=0
for i in d:
    if prime(i):
        c+=i
        h+=1
av=c/h
avg="{:.2f}".format(av)
print(avg)
