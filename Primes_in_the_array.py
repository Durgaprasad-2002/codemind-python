n=int(input())
d=list(map(int,input().split()))
l=len(d)
c=0
for i in range(0,l):
    s=d[i]
    c1=0
    for j in range(1,s):
        if s%j==0:
            c1+=1
    if c1==1:
        c+=1
print(c)