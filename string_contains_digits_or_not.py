d='1234567890'
n=int(input())
for i in range(0,n):
    s=input()
    h=0
    for i in s:
        if i in d:
            h=1
            print("Yes")
            break
    if h==0:
        print("No")