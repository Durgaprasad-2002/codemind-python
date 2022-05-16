d=list(map(str,input().split()))
d1=[]
for i in range(len(d)):
    if i==0:
        n=d[i]
        n=list(n)
        n.reverse()
        n=''.join(n)
        d1+=[n]
    elif i%2==0:
        n=d[i]
        n=list(n)
        n.reverse()
        n=''.join(n)
        d1+=[n]
    elif i%2!=0:
        n=d[i]
        d1+=[n]
print(*d1)
        
        