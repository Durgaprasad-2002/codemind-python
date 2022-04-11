n=int(input())
s=str(n)
s=list(s)
i =0
l = len(s)

while True:
    if i>=l:
        print(n)
        break
        
    if s[i]=='6':
        s[i]='9'
        s=''.join(s)
        s=int(s)
        print(s)
        break
    i+=1