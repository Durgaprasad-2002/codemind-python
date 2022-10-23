n=input()
n=list(n)
for i in range(0,len(n)):
    if n[i]=='.':
        n[i]='[.]'
print(''.join(n))