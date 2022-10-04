n=int(input())
for i in range(0,n):
    n,k=map(int,input().split())
    d=list(map(int,input().split()))
    i=0
    while i<k:
        s=d[-1]
        d.remove(s)
        d.insert(0,s)
        i+=1
    print(*d)
        