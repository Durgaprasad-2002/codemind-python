n=int(input())
for i in range(0,n):
    s=input()
    n1=list(s)
    n1.reverse()
    n1=''.join(n1)
    if s==n1:
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")