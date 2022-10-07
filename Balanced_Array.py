n1=int(input())
for i in range(0,n1):
    n=int(input())
    d=list(map(int,input().split()))
    s=sum(d)
    ls=0
    h=0
    for i in range(0,n):
        s-=d[i]
        if ls==s:
            h=1
            print("YES")
            break
        ls+=d[i]
    if h==0:
        print("NO")