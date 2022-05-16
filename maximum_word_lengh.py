n=input()
#print(n)
l=len(n)
c1=0
c=[]
for i in range(l):
    c1+=1
    if i==l-1:
        c+=[c1]
        break
    elif n[i]==' ':
        c+=[c1-1]
        c1=0
print(max(c))