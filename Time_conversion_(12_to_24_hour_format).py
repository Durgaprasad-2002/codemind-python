n=input()
s1=n[0]+n[1]
s2=n[2]+n[3]+n[4]
s3=n[6]+n[7]
s1=int(s1)
n1=''
if s3=='AM':
    if s1==12:
        n1+='0'
        n1+='0'
    elif s1<=9:
        n1+='0'
        n1+=str(s1)
    else:
        n1+=str(s1)
else:
    if s1==12:
        n1+=str(12)
    elif s1<=9:
        n1+=str(s1+12)
    else:
        n1+=str(s1+12)
n1+=s2
print(n1)