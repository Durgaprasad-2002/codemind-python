n=int(input())
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
def before(n):
    for i in range(n-1,0,-1):
        if palin(i):
            return i
def after(n):
    i=n+1
    while True:
        if palin(i):
            return i
        i+=1
bnum=before(n)
anum=after(n)
d1=n-bnum
d2=anum-n
if (d1>d2):
    print(anum)
elif(d2>d1):
    print(bnum)
else:
    print(bnum,anum)