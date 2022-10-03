n=int(input())
d=list(map(int,input().split()))
k=int(input())
c=[]
for i in range(0,len(d)):
    s=d[i]
    if s+k>=max(d):
        c.append("True")
    else:
        c.append("False")
print(*c)