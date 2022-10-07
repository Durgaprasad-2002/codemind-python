n=int(input())
d=list(map(int,input().split()))
for i in range(0,n):
    if d[i]==0:
        d.remove(d[i])
        d.insert(0,0)
    elif d[i]==1:
        d.remove(d[i])
        d.append(1)
print(*d)