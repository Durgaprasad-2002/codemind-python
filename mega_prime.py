n=int(input())
c=1
i=2
while n:
    if n%i==0:
        c+=1
    if i>n:
        break
    i+=1

    
if c==2:
    s=[]
    i=1
    while n:
        d=n%10
        n=n//10
        s+=[d]
    l=len(s)#3
    a=0
    g=0
    i=0
    while True:
        if i>=l:
            break
        
        a=s[i]
        a=int(a)
        k=0
        j=2
        while True:
            if a%j==0: 
                k+=1
            if j>a:
                if k==1: 
                    g+=1 
                    k=0
                break
            j+=1

        i+=1
    if g==l:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')
        
