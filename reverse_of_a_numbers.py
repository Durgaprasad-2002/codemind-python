n=int(input())
if n<0:
    n=n//-1
    string=str(n)
    string=list(string)
    string.reverse()
    string= ''.join(string)
    num=int(string)
    num=-1*num
    print(num)
else:
    string=str(n)
    string=list(string)
    string.reverse()
    string= ''.join(string)
    num=int(string)
    print(num)
    

