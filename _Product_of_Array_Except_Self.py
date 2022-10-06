n=int(input())
d=list(map(int,input().split()))
f=[]
for i in range(0,n):
    p=1
    for j in range(0,n):
        if j!=i:
            p*=d[j]
    f.append(p)
print(*f)