n=int(input())
for i in range(0,n):
    d=int(input())
    d=str(d)
    r=list(map(int,str(d)))
    r.sort()
    s=r[0]+1
    j=1
    h=0
    while j<len(r):
        if r[j]!=s:
            h=1
            print("NO")
            break
        s+=1
        j+=1
    if h==0:
        print("YES")