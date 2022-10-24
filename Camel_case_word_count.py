n=input()
c='QWERTYUIOPASDFGHJKLZXCVBNM'
if n[0] in c:
    count=0
else:
    count=1
for i in n:
    if i in c:
        count+=1
print(count)