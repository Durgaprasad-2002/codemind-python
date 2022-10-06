n1=int(input())
d1=list(map(int,input().split()))
n2=int(input())
d2=list(map(int,input().split()))
d1.sort()
d2.sort()
if d1==d2:
    print("True")
else:
    print("False")