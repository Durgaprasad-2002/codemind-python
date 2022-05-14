n=int(input())
d=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,n):
    if i>(n/2)-1:
        s2+=d[i]
    else:
        s1+=d[i]
print(s1)
print(s2)