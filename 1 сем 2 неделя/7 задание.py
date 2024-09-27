a = input().split()
b = 0
for i in range(len(a)):
    if a.count(a[i]) > b:
        b = int(a[i])
print(b)

