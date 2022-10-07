n=int(input())
i1=0
i2=n-1
s1=0
s2=0
for i in range(0,n):
    d=list(map(int,input().split()))
    s1+=d[i1]
    s2+=d[i2]
    i1+=1
    i2-=1
st1="Principal Diagonal:"
st1+=str(s1)
st2="Secondary Diagonal:"
st2+=str(s2)
print(st1)
print(st2)