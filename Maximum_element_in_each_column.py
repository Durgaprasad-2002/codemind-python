r,c=map(int,input().split())
d1=[]
for i in range(0,r):
    d=list(map(int,input().split()))
    d1.append(d)
for j in range(0,c):
    f=[]
    for i in d1:
        s=i
        f.append(s[j])
    print(max(f))
    
    