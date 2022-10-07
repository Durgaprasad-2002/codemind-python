r=int(input())
c=int(input())
s=0
for i in range(0,r):
    d=list(map(int,input().split()))
    s+=sum(d)
print(s)
    
    