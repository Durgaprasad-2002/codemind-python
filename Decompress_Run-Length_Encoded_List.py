n=int(input())
d=list(map(int,input().split()))
m=[]
for i in range(0,n,2):
    a=d[i]
    b=d[i+1]
    for i in range(0,a):
        m.append(b)
print(*m)