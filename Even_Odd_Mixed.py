def digits(n):
    ec=0
    oc=0
    i=0
    while (n>0):
        d=n%10
        n=n//10
        if d%2==0:
            ec+=1
        else:
            oc+=1
        i+=1
    return ec,oc
n=int(input())
ec,oc=digits(n)
if ec>0 and oc==0:
    print("Even")
elif ec==0 and oc>0:
    print("Odd")
else:
    print("Mixed")