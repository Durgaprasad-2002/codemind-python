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
    print('prime')
else:
    print('not a prime')
        