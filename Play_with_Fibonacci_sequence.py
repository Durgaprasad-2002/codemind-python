n=int(input())
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a," ",b)
else:
    d=[a,b]
    i=3
    while i<=n:
        c=a+b
        d.append(c)
        a=b
        b=c
        i+=1
    print(*d)