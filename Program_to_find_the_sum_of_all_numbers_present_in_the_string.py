n=input()
num='123456789'
s=0
for i in n:
    if i in num:
        s+=int(i)
print(s)