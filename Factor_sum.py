n1=input()
n=[]
for i in n1:
    if i!=",":
        n.append(int(i))
def fact(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
f=[]
h=0
for i in n:
    r=fact(i)
    if r in n:
        h=1
        f.append(i)
f.sort()
if h==0:
    print(-1)
else:
    print(*f)
    