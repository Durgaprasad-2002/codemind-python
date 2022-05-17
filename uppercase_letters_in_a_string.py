s="QWERTYUIOPASDFGHJKLZXCVBNM"
n=input()
c=0
for i in n:
    if i in s:
        c+=1
print(c)