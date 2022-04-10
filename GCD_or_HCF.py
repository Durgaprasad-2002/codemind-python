def find_gcd(x,y):
    while y:
        if x>y:
            x,y=y,x
        
        y=y%x
    return x




a,b=map(int,input().split())
gcd=find_gcd(a,b)
print(gcd)