n=int(input())
d=list(map(int,input().split()))
s2=0
for i in range(0,n):
    if d[i]%2!=0:
        break
    s2+=d[i]
print(s2)