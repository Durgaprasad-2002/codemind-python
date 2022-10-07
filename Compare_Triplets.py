d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,len(d1)):
    if d1[i]>d2[i]:
        s1+=1
    elif d1[i]<d2[i]:
        s2+=1
c=[]
c.append(s1)
c.append(s2)
print(*c)