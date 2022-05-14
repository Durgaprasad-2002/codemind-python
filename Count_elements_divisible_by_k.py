n,k=map(int,input().split())
d=list(map(int,input().split()))
c=0
for i in range(0,n):
    if d[i]%k==0:
        c+=1
print(c)