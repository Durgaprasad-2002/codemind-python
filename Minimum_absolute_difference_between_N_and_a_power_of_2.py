import math
n=int(input())
i=1
h=0
while True:
    s=int(math.pow(2,i))
    if s>n:
        break
    h=s
    i+=1
l=h
r=l*2
a=n-l
b=r-n
if a<b:
    print(a)
else:
    print(b)