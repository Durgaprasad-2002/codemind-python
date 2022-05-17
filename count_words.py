n=list(map(str,input().split()))
s1="aeiouAEIOU"
s2="qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
c=0
for i in n:
    d=[]
    d=list(i)
    l=len(d)
    if d[0] in s1 and d[l-1] in s2:
        c+=1
print(c)

        