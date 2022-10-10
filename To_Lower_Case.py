c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s='abcdefghijklmnopqrstuvwxyz'
c=list(c)
s=list(s)
n=input()
n1=''
for i in n:
    if i in c:
        i1=c.index(i)
        n1+=s[i1]
    else:
        n1+=i
print(n1)
