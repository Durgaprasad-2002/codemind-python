n=int(input())
d=list(map(int,input().split()))
l=len(d)
f=[]
for i in range(0,l-1,2):
    s=d[i]
    for j in range(0,d[i+1]):
        h=s
        f.append(h)
print(*f)
    
