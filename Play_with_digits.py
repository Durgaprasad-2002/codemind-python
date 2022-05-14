n=int(input())
d=list(map(int,input().split()))
d1=[]
for i in range(0,n):
    if d[i]>9:
        j=1
        s=d[i]
        while s:
            d2=s%10
            s=s//10
            d1+=[d2]
            j+=1
    else:
        d1+=[d[i]]
            
print(sum(d1))
            
            