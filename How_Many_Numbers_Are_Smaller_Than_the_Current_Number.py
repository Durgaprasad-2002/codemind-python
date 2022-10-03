n=int(input())
d=list(map(int,input().split()))
c1=[]
for i in d:
    c=0
    for j in d:
        if j<i:
            c+=1
    c1.append(c)
print(*c1)