n=int(input())
d=[]
for i in range(0,n):
    d1=list(map(int,input().split()))
    d.append(d1)
for j in d:
    s=j
    c=0
    for i in range(s[0],s[1]+1):
        d=i%10
        if (d==2 or d==3 or d==9):
            c+=1
            
    print(c)
    