n=int(input())
d=list(map(int,input().split()))
c=[]
for i in d:
    if d.count(i)==1:
        c.append(i)
if len(c)>0:
    print(*c)
else:
    print(-1)