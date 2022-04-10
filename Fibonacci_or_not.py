n=int(input())
a=0
b=1
if a==n or b==n:
    print('True')
else:
    i=3
    while True:
        c=a+b
        if c==n:
            print('True')
            break
        a=b
        b=c
        if c>n:
            print('False')
            break
        i+=1