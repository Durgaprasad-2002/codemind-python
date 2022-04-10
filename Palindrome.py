n=int(input())
string=str(n)
string=list(string)
string.reverse()
string= ''.join(string)
num=int(string)
if n==num:
    print('True')
else:
    print('False')