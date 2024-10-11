a = [3,5,7,2,55,6,4,4,4,4,4678,2,4,5,67,9,90,899,9,0,45,45,544,1,2,3,4,5,6,7,8,9,0,66,544,7,33]
b = [2,69,0,54,4,90,77,533,6778,45,6,78,3,3,5,98,76,78,4,5,67,8,8,4,2,2,5,7,8,3,35,5,22,5,689]
n =[]
x =[]
m =[]
for i in range(len(a)):
    if not (a[i] in a[:i]+a[i+1:]):
        n.append(a[i])   
for j in range(len(b)):
    if not (b[j] in b[:j]+b[j+1:]):
        x.append(b[j])
c = a+b
for k in range(len(c)):
     if not (c[k] in c[:k]+c[k+1:]) :
        m.append(k)
print(n, x, m, sep='\n')
    






