n=int(input())
a=[]
c=0
i=0
while n:
    d=n%10
    n=n//10
    a+=[d]
    c+=1
    i+=1

res=[]
for i in a:
    if i not in res:
        res.append(i)


s=len(res)   
if c==s:
    print('Unique Number')
else:
    print('Not Unique Number')
