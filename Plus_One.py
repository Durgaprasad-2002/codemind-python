n=int(input())
d=list(map(int,input().split()))
s=""
for i in d:
    s+=str(i)
s=int(s)+1
s=str(s)
r=[int(x) for x in str(s)]
print(*r)