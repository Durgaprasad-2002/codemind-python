n=input()
k="aeiou"
k1="AEIOU"
h=[]
for i in n:
    if i in h:
        continue
    elif i in k:
        h+=[i]
    elif i in k1:
        h+=[i]
if len(h)==0:
    print(-1)
else:
    print(*h)
        

    