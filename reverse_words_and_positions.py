d=list(map(str,input().split()))
d.reverse()
d1=[]
for i in d:
    n=i
    n=list(n)
    n.reverse()
    n=''.join(n)
    d1+=[n]
print(*d1)
    
    