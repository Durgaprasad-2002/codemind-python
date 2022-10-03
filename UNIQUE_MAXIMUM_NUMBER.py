n=int(input())
d=list(map(int,input().split()))
s=set(d)
s=list(s)
d1=[]
for i in s:
    c=d.count(i)
    if c==1:
        d1.append(i)
if len(d1)>=1:
    print(max(d1))
else:
    print(-1)