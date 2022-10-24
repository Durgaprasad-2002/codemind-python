n=input()
k=input()
n=list(n)
c=n.count(k)
if c==0:
    print(-1)
else:
    print(c)