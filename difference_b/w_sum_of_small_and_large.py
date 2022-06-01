d=list(map(str,input().split()))
c1=0
c2=0
for i in d:
    a=max(i)
    b=min(i)
    c1+=ord(a)
    c2+=ord(b)
if c1>c2:
    print(c1-c2)
else:
    print(c2-c1)