d=list(map(str,input().split()))
d1=[]
for i in range(len(d)):
    n=d[i]
    n=list(n)
    n.reverse()
    n=''.join(n)
    d1+=[n]
print(*d1)
        
        