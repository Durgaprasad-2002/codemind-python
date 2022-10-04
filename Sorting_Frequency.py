n=int(input())
d=list(map(int,input().split()))
s=set(d)
s=list(s)
c=[]
for i in s:
    c1=d.count(i)
    c.append(c1)
f=[]
while len(c)>0:
    m=max(c)
    i1=c.index(m)
    c.remove(m)
    f.append(s[i1])
    s.remove(s[i1])
print(*f)