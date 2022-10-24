n=input()
al='abcdefghijklmnopqrstuvwxyz'
al=list(al)
h=0
for i in range(0,len(n)):
    if n[i] in al:
        if al.index(n[i])>h:
            h=al.index(n[i])
print(al[h])