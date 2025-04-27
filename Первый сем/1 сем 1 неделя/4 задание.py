f = open('input.txt', 'r')
f1 = open('output.txt', 'w')
c=f.readlines()
a = list(map(int, c[0].split()))
b = list(c[1].split())
s=0
s1=1
if b[0]=='+':
    for i in range(len(a)):
        s+=a[i]
    print(f1.write(str(s)))
if b[0]=='-':
    for i in range(len(a)):
        if i==0:
            s=a[i]
        else:
            s-=a[i]
    print(f1.write(str(s)))
if b[0]=='*':
    for i in range(len(a)):
        s1*=a[i]
    print(f1.write(str(s1)))
f1.close()
