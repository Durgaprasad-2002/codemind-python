n=int(input())
d=list(map(int,input().split()))
g=[]
for i in range(n):
    if i>=int(n//2):
        break
    g.append(d[i])
    g.append(d[(n-1)-i])
if n%2!=0:
    g.append(d[i])
    g.append(0)
print(*g)