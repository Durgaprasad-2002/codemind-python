n=int(input())
s=0
i=1
while True:
    s=i*(i+1)
    if s==n:
        print('YES')
        break
    if i>n/2:
        print('NO')
        break
    i+=1