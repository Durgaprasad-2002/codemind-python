d=list(map(str,input().split()))
c1=0
c2=0
c=[]
for i in d:
    c1=0
    c2=0
    a=max(i)
    b=min(i)
    c1+=ord(a)
    c2+=ord(b)
    
    if c1>c2:
        c+=[c1-c2]
    else:
        c+=[c2-c1]
print(*c)