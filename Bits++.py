n=int(input())
d=''
for i in range(0,n):
    a=input()
    d+=a
s1='++X'
s2='X++'
s3='--X'
s4='X--'
c=0
for i in range(0,len(d),3):
    s=''
    s=d[i]+d[i+1]+d[i+2]
    if s==s1 or s==s2:
        c+=1
    elif s==s3 or s==s4:
        c-=1
print(c)