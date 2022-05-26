n=int(input())
c=[]
for i in range(n):
	c.append("x")
g=c
for j in range(n):
	d=list(g)
	d.remove(d[j])
	d.insert(j,"0")
	print(''.join(d))