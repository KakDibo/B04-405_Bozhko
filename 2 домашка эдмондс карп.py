from collections import deque

def find_augmenting_path(network, source, sink):
    parents = {}
    flow = {source: float('inf')}
    active = deque([source])
    
    while active:
        current = active.popleft()
        for neighbor, capacity in network[current].items():
            residual = capacity
            if residual > 0 and neighbor not in parents:
                parents[neighbor] = current
                flow[neighbor] = min(flow[current], residual)
                if neighbor == sink:
                    return parents, flow[sink]
                active.append(neighbor)
    return None, 0

def update_network(network, path, flow_value, source, sink):
    node = sink
    while node != source:
        prev = path[node]
        network[prev][node] -= flow_value
        network[node][prev] += flow_value
        node = prev

def compute_max_flow(network, source, sink):
    total_flow = 0
    while True:
        path, flow_amount = find_augmenting_path(network, source, sink)
        if not path:
            break
        update_network(network, path, flow_amount, source, sink)
        total_flow += flow_amount
    return total_flow

print(compute_max_flow(G, '0', '5'))
