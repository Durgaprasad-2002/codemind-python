n=int(input())
def palin(n):
    num=str(n)
    num=list(num)
    num.reverse()
    num=''.join(num)
    num=int(num)
    return num
i=0
x=n
while True:
    rn=palin(x)
    x+=rn
    r=palin(x)
    if x==r:
        print(x)
        break
    i+=1