s1="abcdefghijklmnopqrstuvwxyz"
s2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s1=list(s1)
s2=list(s2)
d=input()
c1=0
c2=0
h1=100
h2=100
for i in d:
    if i in s1:
        c1=s1.index(i)
        if c1<h1:
            h1=c1
    elif i in s2:
        c2=s2.index(i)
        if c2<h2:
            h2=c2
if h1>h2:
    print(s2[h2])
elif h2>h1:
    print(s1[h1])
elif h1==h2:
    print(s1[h1])
    