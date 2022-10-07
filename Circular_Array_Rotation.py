n,r,q=map(int,input().split())
d=list(map(int,input().split()))
q1=[]
for i in range(0,q):
    a=int(input())
    q1.append(a)
for i in range(0,r):
    s=d[-1]
    d.remove(s)
    d.insert(0,s)
for i in q1:
    print(d[i])