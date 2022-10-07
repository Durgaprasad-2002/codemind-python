n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    d1=list(map(int,input().split()))
    d2=list(map(int,input().split()))
    d=d1+d2
    d.sort()
    print(*d)