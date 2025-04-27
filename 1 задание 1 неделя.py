n, m = map(int, input().split())
g = {i: set() for i in range(n)}

d = [0] * n
s = 0
for e in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
    if e == 0:
        s = a
    d[a] += 1
    d[b] += 1

od = []
oc = 0
for i in range(n):
    if d[i] % 2 != 0:
        oc += 1
        od.append(i)

v = []
def f(g, v, s):
    v.append(s)
    for nb in g[s]:
        if nb not in v:
            f(g, v, nb)

c = []
f(g, v, s)

if oc == 2 and len(v) == n:
    r = []  
    def b(curr):
        while g[curr]:
            nxt = g[curr].pop()
            g[nxt].remove(curr)
            b(nxt)
        r.append(curr)

    b(od[0])
    print(*r[::-1])
else:
    print('no way')