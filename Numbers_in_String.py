n=input()
num='0123456789'
n+='@'
s=0
for i in range(0,len(n)):
    if n[i] in num:
        s+=int(n[i])
print(s)