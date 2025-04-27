from collections import defaultdict

def g(e):
    d = defaultdict(set)
    for _ in range(e):
        a, b = input().split()
        d[a].add(b)
        d[b].add(a)
    return d

def f(g, u, v, m):
    v.add(u)
    for n in g[u]:
        if n not in v:
            if not m.get(n):
                m[u], m[n] = n, u
                return 1
            elif f(g, m[n], v, m):
                m[u], m[n] = n, u
                return 1
    return 0

def k(g):
    m = {}
    for x in g:
        if x not in m:
            f(g, x, set(), m)
    return m

def c(g, m):
    cv = set(m) - {y for y in m if not m[y]}
    av = set(g)
    uv = av - cv
    
    ec = set()
    for a, b in m.items():
        if b:
            ec.add(tuple(sorted((a, b))))
    
    for x in uv:
        for y in g[x]:
            ec.add(tuple(sorted((x, y))))
            break
    
    return ec

def main():
    e = int(input())
    gr = g(e)
    mt = k(gr)
    res = c(gr, mt)
    print(res)
main()