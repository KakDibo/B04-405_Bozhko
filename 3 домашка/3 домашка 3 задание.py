def z_to_word(z):
    if not z:
        return ''
    
    res = [''] * len(z)
    res[0] = 'A'
    left, right = 0, 0
    char = 66

    for i in range(1, len(z)):
        if i > right:
            if z[i] == 0:
                res[i] = chr(char)
                char += 1
                left, right = i, i
            else:
                for j in range(z[i]):
                    if i + j >= len(z):
                        break
                    res[i+j] = res[j]
                left, right = i, i + z[i] - 1
        else:
            pos = i - left
            if z[pos] < right - i + 1:
                res[i] = res[pos]
            else:
                for j in range(right - i + 1, z[pos]):
                    if i + j >= len(z):
                        break
                    res[i+j] = res[j]
                left, right = i, i + z[pos] - 1

    return ''.join(res)

print(z_to_word([0,0,1,0,3,0,1]))