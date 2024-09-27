a = list(map(int, input().split()))
b = [i for i in range(1, len(a)+1)]
for i in range(len(b)):
    if b[i] not in a[1::]:
        print(b[i])
