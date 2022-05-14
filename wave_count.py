n=int(input())
d=list(map(int,input().split()))
s=d[1]
a=d[0]
l=len(d)
h=0
g=0
for i in range(1,l-1):
    if a<s:
        h=1
        s=d[i+1]
        a=d[i]
    else:
        h=2
        s=d[i+1]
        a=d[i]
    if h==1:
        if s<a:
            s=d[i+1]
            a=d[i]
        else:
            g=1
            break
    if h==2:
        if a<s:
            s=d[i+1]
            a=d[i]
        else:
            g=1
            break
if g==0:
    c=0
    if h==1:
        for i in range(1,l-1):
            if d[i-1]<d[i]>d[i+1]:
                c+=1
    if h==2:
        for i in range(1,l-1):
            if d[i-1]>d[i]<d[i+1]:
                c+=1
                
    
if g==1:
    print("-1")
else:
    print(c)
        
        
    
