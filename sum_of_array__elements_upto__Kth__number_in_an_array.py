n=int(input())
d=list(map(int,input().split()))
k=int(input())
s2=0
for i in range(0,n):
    s2+=d[i]
    if d[i]==k:
        break
print(s2)