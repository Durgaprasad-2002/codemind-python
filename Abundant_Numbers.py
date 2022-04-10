n=int(input())
k=n
s=0
i=1
while True:
    if n%i==0:
        s+=i
    if i>n/2:
        break
    i+=1
if s>k:
    print('True')
else:
    print('False')