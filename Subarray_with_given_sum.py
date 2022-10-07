n=int(input())
for z in range(0,n):
    n,k=map(int,input().split())
    d=list(map(int,input().split()))
    j=0
    h=0
    while j<n:
        s=0
        for i in range(j,n):
            s+=d[i]
            if s==k:
                h=1
                print(j+1,i+1)
                break
        if h==1:
            break
        j+=1
    if h==0:
        print(-1)