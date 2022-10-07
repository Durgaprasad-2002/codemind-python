n=int(input())
d=list(map(int,input().split()))
s=set(d)
s=list(s)
s.sort()
c=[]
for i in s:
    c1=d.count(i)
    c.append(c1)
i1=c.index(max(c))
print(s[i1])