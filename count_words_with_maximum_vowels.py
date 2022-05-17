n=input()
s1="aeiouAEIOU"
d=list(n)
c=0
c1=[]
h=0
for i in d:
    if i in s1:
        c+=1
    if i is ' ':
        h=1
        c1+=[c]
        c=0
if h==1:
    c1+=[c]
    m=max(c1)
    mn=c1.count(m)
    print(mn)
else:
    print(1)