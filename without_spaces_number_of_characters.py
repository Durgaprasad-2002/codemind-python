n=input()
d=list(n)
c=0
for i in d:
    if i is ' ':
        c+=1
l=len(d)-c
print(l)