import random

def rk(s, t):
    count = 0
    q = 2**13-1
    x = random.randint(3,q-1)
    
    shifts = {s[i:] + s[:i]:None for i in range(len(s))}
    for shift in shifts:
        h = ord(shift[0]) % q
        for c in shift[1:]:
            h = (x * h + ord(c)) % q
        shifts[shift] = h
    
    h_t = [0]*(len(t)+1)
    for i in range(len(t)):
        h_t[i+1] = (x * h_t[i] + ord(t[i])) % q
    
    n = len(s)
    x_pow = pow(x, n, q)
    for i in range(len(t)-n+1):
        window_hash = (h_t[i+n] - x_pow * h_t[i]) % q
        if window_hash in shifts.values():
            count += 1
            
    return count

print(rk('abc', 'abcabacbacababc'))