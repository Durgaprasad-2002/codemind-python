n=int(input())
##d=[ ]
##for i in range(n):
##    val=int(input())
##    d.append(val)
d=list(map(int,input().split()))
os=0
for i in range(0,n):
    s=d[i]
    s=int(s)
    if i%2!=0:
        os+=s
print(os)
