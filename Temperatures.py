n=int(input())
d=list(map(int,input().split()))
t=[]
for i in range(0,n):
    s1=d[i]
    c1=0
    h=0
    j=i+1
    while j<n:
        c1+=1
        if d[j]>s1:
            h=1
            break
        j+=1
    if h==1:
        c=c1
    else:
        c=0
    t.append(c)
print(*t)