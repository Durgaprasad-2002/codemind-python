n=int(input())
d=list(map(int,input().split()))
def even(n):
    c=0
    while n>0:
        d=n%10
        c+=1
        n=n//10
    if c%2==0:
        return True
    else:
        return False
c=0
for i in d:
    if even(i):
        c+=1
if c==0:
    print(-1)
else:
    print(c)