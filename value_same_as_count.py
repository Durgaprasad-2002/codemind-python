n=int(input())
d=list(map(int,input().split()))
#print(n)
#print(d)
s=set(d)
s=list(s)
l=len(s)
c=0
for i in s:
    k=d.count(i)
    if i==k:
        c+=1
print(c)