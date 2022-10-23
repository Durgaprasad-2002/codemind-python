n=input()
n+='0'
n=list(n)
d=[]
c=1
for i in range(0,len(n)-1):
    if n[i]==n[i+1]:
        c+=1
    else:
        d.append(c)
        c=1
print(max(d))