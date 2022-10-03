a=int(input())
b=int(input())
m=a+b
c=m
for i in range(1,c+1):
    c+=1
    k=0
    for j in range(1,(c//2)+1):
        if c%j==0:
            k+=1
    if k==1:
        print(c-m)
        break
        