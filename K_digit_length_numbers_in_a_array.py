n,k=map(int,input().split())
d=list(map(str,input().split()))
c=0
for i in d:
    i=int(i)
    if i<0:
        i=i//-1
    i=str(i)
    l=len(i)
    if l==k:
        c+=1
print(c)