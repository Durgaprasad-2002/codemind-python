def back(s):
    s=list(s)
    i1=s.index('#')
    s.remove(s[i1-1])
    s.remove('#')
    return ''.join(s)
s1=input()
s2=input()
i=0
while True:
    if '#' in s1:
        s1=back(s1)
    if '#' in s2:
        s2=back(s2)
    if '#' not in s1 and '#' not in s2:
        break
if s1==s2:
    print("True")
else:
    print("False")