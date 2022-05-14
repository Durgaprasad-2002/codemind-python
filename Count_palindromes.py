n=int(input())
d=list(map(int,input().split()))
c=0
for i in range(0,n):
    d1=[]
    j=1
    s=d[i]
    while s:
        di=s%10
        s=s//10
        d1+=[str(di)]
        j+=1
    d1=''.join(d1)
    d1=int(d1)
    if d1==d[i]:
        
        c+=1
print(c)
