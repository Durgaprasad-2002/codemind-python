def palin(n):
    num=str(n)
    num=list(num)
    num.reverse()
    num=''.join(num)
    num=int(num)
    if n==num:
        return True
    else:
        return False
l=int(input())
r=int(input())
d=[]
for i in range(l,r+1):
    if palin(i):
        d.append(i)
print(*d)
        