d=list(map(str,input().split()))
c=0
for i in d:
    n=i
    n=list(n)
    s1="AEIOUaeiou"
    s2="QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
    l=len(n)
    for i in range(l//2):
        if n[i] in s1 and n[(l-1)-i] in s2:
            c+=1
        elif n[i] in s2 and n[(l-1)-i] in s1:
            c+=1
print(c)

        