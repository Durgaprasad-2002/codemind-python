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
        
if g==1:
    print("no")
else:
    print("yes")
        
        
    
