n=input()
s1=n[0]+n[1]
s2=n[2]+n[3]+n[4]
s1=int(s1)
n=''
n1=''
if s1>=0 and s1<=11:
    n+=' AM'
else:
    n+=' PM'
s2+=n
if s1==0:
    n1=str(12)
    n1+=s2
elif s1>0 and s1<=12:
    if s1<=9:
        n1+='0'
        n1+=str(s1)
        n1+=s2
    else:
        n1+=str(s1)
        n1+=s2
else:
    if s1-12<=9:
        n1+='0'
        n1+=str(s1-12)
        n1+=s2
    else:
        n1+=str(s1-12)
        n1+=s2
print(n1)
    