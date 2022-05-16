n=int(input())
d=list(map(str,input().split()))
h=[]
for i in d:
    l=len(i)
    h+=[l]
mn=max(h)
c=h.count(mn)
print(c)
    
