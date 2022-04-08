n=int(input())
m=int(input())
s1=0
i=1
while True:
    d=i
    if n%d==0:
        s1+=d
    if i>n/2:
        break
    i+=1
s2=0
i=1
while True:
    d=i
    if m%d==0:
        s2+=d
    if i>m/2:
        break
    i+=1

if n==s2 and m==s1:
    print('Amicable')
else:
    print('Not Amicable')
          
