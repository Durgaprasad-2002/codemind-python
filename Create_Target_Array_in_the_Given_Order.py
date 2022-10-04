n1=int(input())
d1=list(map(int,input().split()))
n2=int(input())
d2=list(map(int,input().split()))
t=[]
for i in range(0,n1):
    i1=d2[i]
    t.insert(i1,d1[i])
print(*t)