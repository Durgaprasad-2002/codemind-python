n=input()
k="aeiou"
k=list(k)
h=0
for i in n:
    if i in k:
        h=1
        k.remove(i)

if len(k)==0:
    print(0)
else:
    print(*k)
    