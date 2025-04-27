import math

def has_profit(g):
    def bf(graph, start):
        dist = {v: math.inf for v in graph}
        dist[start] = 0
        
        for _ in range(len(graph)-1):
            for u in graph:
                for v in graph[u]:
                    if dist[v] > dist[u] + graph[u][v]:
                        dist[v] = dist[u] + graph[u][v]
        
        for u in graph:
            for v in graph[u]:
                if dist[v] > dist[u] + graph[u][v]:
                    return True
        return False
    
    for u in g:
        for v in g[u]:
            g[u][v] = -math.log(g[u][v])
    
    for v in g:
        if bf(g, v):
            return True
    
    return False

n = int(input())
graph = {}

for _ in range(n):
    a, b, rate = input().split()
    rate = float(rate)
    if a not in graph:
        graph[a] = {}
    graph[a][b] = rate

print("Да" if has_profit(graph) else "Нет")