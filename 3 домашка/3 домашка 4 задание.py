def p_to_w(p):
    if not p:
        return ''
    
    w = [''] * len(p)
    w[0] = 'A'
    
    for i in range(1, len(p)):
        if p[i] != 0:
            w[i] = w[p[i] - 1]
        else:
            used = {'A'}
            k = p[i-1]
            
            while k > 0:
                used.add(w[k])
                k = p[k-1]
            
            for c in range(66, 91):
                if chr(c) not in used:
                    w[i] = chr(c)
                    break
    
    return ''.join(w)

print(p_to_w([0, 0, 1, 0, 0, 1]))