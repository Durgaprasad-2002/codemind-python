n=int(input())
s=str(n)
if len(s)==10:
    def digit(n):
        i=0
        while n>0:
            d=n%10
            n=n//10
            i+=1
        return d
    r=digit(n)
    if r!=0:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")