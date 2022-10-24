n=input()
v='aeiou'
d='0123456789'
vc=0
cc=0
dc=0
wc=0
for i in range(0,len(n)):
    if n[i] in v:
        vc+=1
    elif n[i] in d:
        dc+=1
    elif n[i]==' ':
        wc+=1
    else:
        cc+=1
print('Vowels:',vc)
print('Consonants:',cc)
print('Digits:',dc)
print('White spaces:',wc)