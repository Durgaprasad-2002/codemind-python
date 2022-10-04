n=int(input())
d=list(map(int,input().split()))
f1=[]
f=[]
for i in d:
    if i==0:
        f1.append(i)
    else:
        f.append(i)
d1=f+f1
print(*d1)
    