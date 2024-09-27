N =int(input())
a = int(input())
b= int(input())

if(a==10):
    res =''
    while N>0:
        res = str(N%b)+res
        N=N//b

    print(res)
elif (b==10):
    print(int(str(N),a))
else:
    s = int(str(N),a)
    res = ''
    while s > 0:
        res = str(s % b) + res
        s = s // b

    print(res)


