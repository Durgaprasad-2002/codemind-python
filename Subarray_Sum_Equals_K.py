def sub_lists(l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
n,t=list(map(int,input().split()))
d=list(map(int,input().split()))
r=sub_lists(d)
r.remove(r[0])
c=0
for i in r:
    if sum(i)==t:
        c+=1
print(c)