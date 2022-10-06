n=int(input())
d=list(map(int,input().split()))
s=set(d)
s=list(s)
for i in s:
    c1=d.count(i)
    if c1>1:
        print(i)
        break