n=int(input())
d=list(map(int,input().split()))
s=set(d)
s=list(s)
c=0
for i in s:
    if i%2!=0:
        c+=1
print(c)