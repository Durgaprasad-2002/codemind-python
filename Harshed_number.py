n=int(input())
k=n
s=0
i=1
while n:
    d=n%10
    n=n//10
    s+=d
    i+=1
if k%s==0:
    print('True')
else:
    print('False')