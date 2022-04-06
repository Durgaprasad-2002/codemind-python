
n=int(input())
sq=n**2
k=sq
s=0
while k:
    d=k%10
    k=k//10
    s+=d
    
if n==s:
    print('Neon Number')
else:
    print('Not Neon Number')
    
    