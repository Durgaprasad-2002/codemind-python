n=input()
k="aeiou"
k1="AEIOU"
c=0
for i in n:
    if i in k:
        c+=1
    elif i in k1:
        c+=1
print(c)