def factor(n):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s+=i
    return s
n=int(input())
n1=factor(n)
if n==n1:
    print("True")
else:
    print("False")