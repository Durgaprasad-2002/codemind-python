n,m=map(int,input().split())
d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
d1=set(d1)
d1=list(d1)
d2=set(d2)
d2=list(d2)
l1=len(d1)
l2=len(d2)
c=0
for i in range(0,l1):
    s=d1[i]
    if s in d2:
        c+=1
print(c)
