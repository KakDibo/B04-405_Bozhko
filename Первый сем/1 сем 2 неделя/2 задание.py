a = list(input().split())
line_ls = [i for i in a[1]]
b = ''
for i in range(0, len(a[1]), int(a[0])):
    b += ''.join(reversed(line_ls[i:i+int(a[0])]))
print(b)