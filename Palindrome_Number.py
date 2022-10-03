def palin(n):
    string=str(n)
    string=list(string)
    string.reverse()
    string= ''.join(string)
    num=int(string)
    if n==num:
        return True
    else:
        return False
n=int(input())
d=[]
for i in range(0,n):
    a=int(input())
    d.append(a)
for j in d:
    if palin(j):
        print("True")
    else:
        print("False")
