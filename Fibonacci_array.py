n=int(input())
d=list(map(int,input().split()))
l=len(d)
s=d[l-1]
a=d[0]
b=d[1]
c=0
f=[d[0],d[1]]
i=0
while c<s:
    c=a+b
    f.append(c)
    a=b
    b=c
    i+=1
#print(d)
#print(f)
if d==f:
    print("yes")
else:
    print("no")

