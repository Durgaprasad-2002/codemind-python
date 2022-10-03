def digit(n):
    s=0
    i=0
    while n>0:
        d=n%10
        s+=d*d
        n=n//10
        i+=1
    return s
n=int(input())
j=0
r=n
h=0
while j<n*n:
    r=digit(r)
    if (r==1 or r==7):
        h=1
        print("True")
        break
    j+=1
if h==0:
    print("False")