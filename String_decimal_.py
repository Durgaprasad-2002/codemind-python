n=int(input())
for j in range(0,n):
    n=input()
    d='0123456789'
    h=0
    for i in n:
        if i in d:
            continue
        else:
            h=1
            break
    if h==0:
        print("True")
    else:
        print("False")