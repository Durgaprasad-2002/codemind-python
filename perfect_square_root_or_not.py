n=int(input())
i=1
while True:
    s=i**2
    if n==s:
        print('True')
        break
    if i>n/2:
        print('False')
        break
    i+=1   