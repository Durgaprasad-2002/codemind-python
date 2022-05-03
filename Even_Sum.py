n=int(input())
d=list(map(int,input().split()))
es=0
for i in range(0,n):
    s=d[i]
    if s%2==0:
        es+=s
        
print(es)
    
