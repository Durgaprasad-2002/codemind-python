n=int(input())
d1=[]
for i in range(0,n):
    n1=int(input())
    s=list(map(int,input().split()))
    s.sort()
    s.append(0)
    for j in range(1,len(s)):
        if s[j]==s[j-1]+1:
            continue
        else:
            print(s[j-1]+1)
            break
