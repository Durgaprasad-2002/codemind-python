n=int(input())
d=list(map(int,input().split()))
d1=[]
for i in d:
    d1.append(i*i)
d1.sort()
print(*d1)