n=int(input())
s=n*n
e=[]
i=1
d=0
while s:
    d=s%10
    s=s//10
    e+=[d]
    if s==0:
        break
string=str(n)
string=list(string)
string.reverse()
l=len(string)
c=0
j=0
while l:
    if j==l:
        break
    m=string[j]
    n=e[j]
    m=int(m)
    if m==n:
        c+=1
    j+=1

if l==c:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')


