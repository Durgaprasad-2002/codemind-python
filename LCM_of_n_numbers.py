n=int(input())
d=list(map(int,input().split()))
m=max(d)
for j in range(1,m*m):
    c=0
    s=m*j
    for i in d:
        if s%i==0:
            c+=1
    if c==len(d):
        print(s)
        break