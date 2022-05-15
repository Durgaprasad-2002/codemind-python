n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
f=[]
h=0
for i in d:
    if i>=a and i<=b:
        h=1
        f+=[i]
if h==1:
    print(min(f))
else:
    print(-1)
