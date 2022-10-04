n=int(input())
d=list(map(int,input().split()))
s=set(d)
s=list(s)
c=0
h=0
for i in s:
    c1=d.count(i)
    if c1>c:
        c=c1
        h=i
print(h)