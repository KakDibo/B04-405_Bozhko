f = open('input.txt', 'r')
f1 = open('output.txt', 'w')
c=f.readlines()
a = list(map(int, c[0].split()))
b = list(c[1].split())
с = list(map(int, c[2].split()))
s=0
s1=1
if b[0]=='+':
    for i in range(len(a)):
        A = (int(a[i], c))
        s+=A
    print(f1.write(str(s)))
if b[0]=='-':
    for i in range(len(a)):
        A = (int(a[i], c))
        if i==0:
            s=A
        else:
            s-=A
    string = ''
    while s > 0:
        string+=str(s%c)
        s//=c
    print(f1.write(str(string[::-1])))
if b[0]=='*':
    for i in range(len(a)):
        A = (int(a[i], c))
        s1*=A
    string = ''
    while s1 > 0:
        string+=str(s1%c)
        s1//=c
    print(f1.write(str(string[::-1])))
f1.close()


