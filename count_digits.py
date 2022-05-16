n=int(input())
d=list(map(str,input().split()))
c=[]
for i in d:
    i=int(i)
    if i<0:
        i=i//-1
    i=str(i)
    l=len(i)
    c+=[l]
print(*c)