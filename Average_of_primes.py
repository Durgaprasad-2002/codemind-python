m=int(input())
d=list(map(int,input().split()))
m=0
c=0
for i in range(0,len(d)):
    s=d[i]
    c1=0
    for j in range(1,s):
        if s%j==0:
            c1+=1
    if c1==1:
        m+=s
        c+=1
avg=m/c
f="{:.2f}".format(avg)
print(f)
