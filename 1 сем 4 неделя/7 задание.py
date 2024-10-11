import string
s=input()
for i in s:
    if i in string.punctuation:
        s=s.replace(i, " ")
n={}
x=[i.lower() for i in s.split()]
print(x)
for j in x:
    if j in n:
        n[j]+=1
    else:
        n[j]=1
print(n)