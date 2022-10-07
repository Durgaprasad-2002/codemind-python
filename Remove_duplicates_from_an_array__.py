n=int(input())
d=list(map(int,input().split()))
c=[]
for i in d:
    if i not in c:
        c.append(i)
print(*c)        