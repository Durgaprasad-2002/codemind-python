n=int(input())
a=0
b=1
print(a,b,end=' ')
i=3
while True:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    if i==n:
        break
    i+=1