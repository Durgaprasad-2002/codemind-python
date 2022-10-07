n=int(input())
d=list(map(int,input().split()))
n1=[]
n2=[]
for i in range(0,n):
    if i+1<=n//2:
        n1.append(d[i])
    else:
        n2.append(d[i])
n2.reverse()
f=n2+n1
print(*f)