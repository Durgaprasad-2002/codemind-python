def psq(n):
    i=1
    while i*i<=n:
        if i*i==n:
            return True
        i+=1
    return False
n=int(input())
for i in range(0,n):
    a=int(input())
    if psq(a):
        print("True")
    else:
        print("False")