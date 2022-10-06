n=int(input())
d=list(map(int,input().split()))
k=int(input())
if k in d:
    print(d.index(k))
else:
    print(-1)