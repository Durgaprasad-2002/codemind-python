n=input()
n=list(n)
h=0
for i in range(0,len(n)):
    c1=n.count(n[i])
    if c1==1:
        h=1
        print(i)
        break
if h==0:
    print(-1)