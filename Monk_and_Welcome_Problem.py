n=int(input())
d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
for i in range(0,n):
    d2[i]+=d1[i]
print(*d2)