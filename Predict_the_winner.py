n=int(input())
d=list(map(int,input().split()))
x=0
y=0
for i in range(0,len(d)):
    if i%2==0:
        x+=d[i]
    else:
        y+=d[i]
d1=x-y
if d1<0:
    d1=d1//-1
if d1%4==0:
    print("X")
else:
    print("Y")