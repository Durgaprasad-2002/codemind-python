n=int(input())
d=list(map(int,input().split()))
ab=0
es=0
os=0
for i in range(0,n):
    s=d[i]
    if s%2!=0:
        os+=s
    else:
        es+=s
if es>os:
    ab=es-os
else:
    ab=os-es
print(ab)
    
