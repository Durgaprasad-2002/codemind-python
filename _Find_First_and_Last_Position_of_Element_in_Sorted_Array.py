n=int(input())
d=list(map(int,input().split()))
k=int(input())
if k in d:
    for i in range(0,n):
        if d[i]==k:
            i1=i
            break
    for i in range(n-1,-1,-1):
        if d[i]==k:
            i2=i
            break
    print(i1,i2)
else:
    print(-1,-1)