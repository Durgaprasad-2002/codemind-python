n=int(input())
c=[]
for i in range(1,n+1):
    c.append(str(i))
for j in range(n):
    print(''.join(c))
    c.remove(c[-1])
    