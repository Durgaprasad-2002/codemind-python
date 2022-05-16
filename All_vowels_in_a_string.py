n=input()
k="aeiou"
k1="AEIOU"
h=[]
c=0
for i in n:
    if i in h:
        continue
    elif i in k:
        c+=1
        h+=[i]
if c==5:
    print("True")
else:
    print("False")