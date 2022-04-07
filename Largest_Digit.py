n=int(input())
a=[]
i=0
while n:
    d=n%10
    n=n//10
    a+=[d]
    i+=1
    
s=max(a)
print(s)