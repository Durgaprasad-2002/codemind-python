n=input()
n=list(n)
nw=''
v='aeiouAEIOU'
h=len(n)-1
i=0
while i<len(n):
    if n[i] in v:
        if (i<h):
            j=h
            while j>=0:
                if n[j] in v:
                    s=n[i]
                    n[i]=n[j]
                    n[j]=s
                    h=j-1
                    break
                j-=1
    i+=1
print(''.join(n))