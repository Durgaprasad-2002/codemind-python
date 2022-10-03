def digits(n):
    h=n
    c=0
    c1=0
    while n>0:
        d=n%10
        c1+=1
        if d!=0:
            if h%d==0:
                c+=1
        n=n//10
    if c==c1:
        return True
    else:
        return False
l=int(input())
r=int(input())
f=[]
for i in range(l,r+1):
    if digits(i):
        f.append(i)
print(*f)
        