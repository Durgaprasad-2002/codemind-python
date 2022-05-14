n=int(input())
d=list(map(int,input().split()))
d.reverse()
l=len(d)
i=0
h=0
k=0
i=0
while i<l:
    s=d[i]
    if s>h:
        h=s
    else:
        k=1
        break
    i+=1
if k==1:
    print("no")
else:
    print("yes")

