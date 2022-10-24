n=input()
c=1
for i in range(0,len(n)):
    if n[i]==' ' and n[i+1]!=' ':
        c+=1
if len(n)==0:
    print(0)
else:
    print(c)