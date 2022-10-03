def digits(n):
    s=0
    m=1
    while n>0:
        d=n%10
        s+=d
        m*=d
        n=n//10
    return s,m
n=int(input())
s,m=digits(n)
d1=s-m
if d1<0:
    print(d1//-1)
else:
    print(d1)