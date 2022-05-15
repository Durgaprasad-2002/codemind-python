from math import*
def prime(n):
    sq=int(sqrt(n))
    if n==1:
        return False
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if prime(i):
        c+=1
print(c)
