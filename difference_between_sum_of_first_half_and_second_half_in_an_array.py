
n=int(input())
d=list(map(int,input().split()))
s2=0
s1=0
for i in range(0,n):
    if i<=(n/2)-1:
        s1+=d[i]
    else:
        s2+=d[i]
dif=0
if s1>s2:
    dif=s1-s2
else:
    dif=s2-s1
print(dif)