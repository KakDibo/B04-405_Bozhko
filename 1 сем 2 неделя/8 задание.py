n = int(input())
arr = []
s = 0
for i in range(n):
    arr.append(int(input()))
    s = s + arr[i]
mid = int(s / n)
c = []
result = arr[0]
for i in range(n):
    c.append(abs(arr[i] - mid))
    if abs(arr[i] - mid) == min(c):
        result = arr[i]
print(result)

