a,b=map(int,input().split())
g=max(a,b)
k=g
h=min(a,b)
s=g
i=1
while True:
    if g%a==0 and g%b==0:
        print(g)
        break
    else:
        g=k*i
    i+=1
    