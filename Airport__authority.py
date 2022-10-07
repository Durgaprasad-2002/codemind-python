n=int(input())
d=[]
for i in range(0,n):
    a=int(input())
    d.append(a)
t=int(input())
c=0
for i in d:
    if i<=t:
        c+=1
    else:
        c+=2
print(c)
        