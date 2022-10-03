def digit(n):
    s=0
    while n>0:
        d=n%10
        n=n//10
        s+=d
    return s
n=int(input())
i=0
r=n
while True:
    r=digit(r)
    if r<10:
        print(r)
        break
    i+=1