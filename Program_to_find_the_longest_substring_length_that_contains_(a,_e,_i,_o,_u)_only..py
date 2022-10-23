n=input()
n+='0'
v='aeiou'
d=[]
c=1
for i in range(0,len(n)-1):
    if n[i] in v and n[i+1] in v:
        c+=1
    else:
        d.append(c)
        c=1
print(max(d))