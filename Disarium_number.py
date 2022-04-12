n=int(input())
u=n
n=str(n)
l=len(n)
n=int(n)
h=l+1
s=0
i=0
while n:
    d=n%10
    n=n//10
    h-=1
    s+=d**h
    print
    i+=1
 
if u==s:
    print('True')
else:
    print('False')