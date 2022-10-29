s=input()
s=list(s)
s.insert(0,'.')
s=''.join(s)
d='0123456789'
su=0
for i in range(1,len(s)):
    if s[i] in d:
        if s[i-1]=='+':
            su+=int(s[i])
        elif s[i-1]=='-':
            su-=int(s[i])
        else:
            su+=int(s[i])
print(su)