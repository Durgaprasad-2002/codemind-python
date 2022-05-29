n=list(map(str,input().split()))
c=[]
for i in n:
    c.append(min(i))
    c.append(max(i))
print(*c)
    