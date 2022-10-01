def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
n=int(input())
for i in range(0,n):
    a=int(input())
    print(fact(a))