n=int(input())
d=list(map(str,input().split()))
h=[]
for i in d:
    h+=[len(i)]
mx=max(h)
h=[]
for i in d:
    if len(i)==mx:
        h+=[i]
print(*h)