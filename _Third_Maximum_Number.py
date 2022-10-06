k=int(input())
nums=list(map(int,input().split()))
n=[]
for i in nums:
    if i not in n:
        n.append(i)
if len(n)>=3:
    for i in range(0,3):
        m=max(n)
        n.remove(m)
    print(m)
else:
    print(max(n))