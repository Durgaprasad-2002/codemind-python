n=int(input())
d=list(map(int,input().split()))
m=min(d)
i=0
while n>=1:
    c=0
    for i in d:
        if i%m==0:
            c+=1
    if c==len(d):
        print(m)
        break
    m-=1
    i+=1