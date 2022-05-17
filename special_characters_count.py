s1="!@#$%^&*()_+.,<>/?;:\|-="
n=input()
c=0
for i in n:
    if i in s1:
        c+=1
print(c)