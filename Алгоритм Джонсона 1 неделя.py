import heapq

a, b = map(int, input().strip().split())
g = {}
for _ in range(b):
    c, d, e = map(int, input().strip().split())
    if c not in g:
        g[c] = {}
    if d not in g:
        g[d] = {}       
    g[c][d] = e  

def bf(g, s):
    d = {i: float('inf') for i in range(a)}
    d[s] = 0
    for _ in range(a - 1):
        for i in g:
            for j in g[i]:
                if d[j] > d[i] + g[i][j]:
                    d[j] = d[i] + g[i][j]
    return d

def dj(g, s):
    d = {i: float('infinity') for i in range(a)}
    d[s] = 0
    h = [(0, s)]
    while h:
        cd, cn = heapq.heappop(h)
        if cd > d[cn]:
            continue
        for nb in g[cn]:
            dist = cd + g[cn][nb]
            if dist < d[nb]:
                d[nb] = dist
                heapq.heappush(h, (dist, nb))
    return d

def j(g):
    nv = a
    g[nv] = {}
    for n in range(a):
        g[nv][n] = 0  
    p = bf(g, nv)
    ng = {n: {} for n in range(a)}
    for u in g:
        for v in g[u]:
            if u != nv and v != nv:
                nw = g[u][v] + p[u] - p[v]
                ng.setdefault(u, {})[v] = nw
    ad = {}
    for n in range(a):
        ad[n] = dj(ng, n)
    for u in ad:
        for v in ad[u]:
            ad[u][v] += p[v] - p[u]

    return ad

r = j(g)
for i in range(a):
    line = []
    for k in range(a):
        if r[i][k] == float('inf'):
            line.append('inf')
        else:
            line.append(str(r[i][k]))
    print(' '.join(line))