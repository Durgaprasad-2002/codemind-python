n=input()
d=list(n)
s1=d.count('z')
s2=d.count('o')
if s1*2==s2:
    print("Yes")
else:
    print("No")