n=int(input())
s=0
m=1
while n:
    d=n%10
    n=n//10
    s+=d
    m*=d
    
if s==m:
    print('Spy Number')
else:
    print('Not Spy Number')