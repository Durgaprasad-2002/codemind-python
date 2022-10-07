n,k=map(int,input().split())
d=list(map(int,input().split()))
c=0
h=0
for i in range(0,n):
    if d[i]<=k:
        c+=1
        continue
    elif d[i]>k and h==0:
        h=1
        continue
    elif d[i]>k and h==1:
        break
print(c)