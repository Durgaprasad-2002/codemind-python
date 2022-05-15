n=int(input())
d=list(map(int,input().split()))
s=set(d)
s=list(s)
l=len(s)
c=0
c1=[]
for i in s:
    k=d.count(i)
    if i==k:
        c=1
        c1+=[i]
if c==1:
    print(min(c1),max(c1))
else:
    print(-1)
