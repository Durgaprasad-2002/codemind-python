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
        
l2=len(c1)        
if c==1:
    av=sum(c1)/l2
    avg="{:.2f}".format(av)
    print(avg)
else:
    print(-1)
