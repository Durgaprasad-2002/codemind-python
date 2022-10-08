n=input()
vowels="AEIOUaeiou"
o=[1]
for i in n:
    l=len(o)-1
    if i in vowels:
        if o[l]=='V':
            continue
        else:
            o.append('V')
    else:
        if o[l]=='C':
            continue
        else:
            o.append('C')
o.remove(o[0])
o=''.join(o)
print(o)