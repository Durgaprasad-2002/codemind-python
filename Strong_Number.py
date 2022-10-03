def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
def digit(n):
    d=[]
    while (n>0):
        d1=n%10
        n=n//10
        r=fact(d1)
        d.append(r)
    return sum(d)
n=int(input())
r1=digit(n)
if n==r1:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")