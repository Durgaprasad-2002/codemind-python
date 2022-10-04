n1=int(input())
d1=list(map(int,input().split()))
n2=int(input())
d2=list(map(int,input().split()))
e=int(input())
c=0
for i in range(0,n1):
    if d1[i]<= e and e<=d2[i]:
        c+=1
print(c)