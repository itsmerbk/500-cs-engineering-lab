def color_graph(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    colors = [-1]*n
    for u in range(n):
        used = {colors[v] for v in adj[u] if colors[v] != -1}
        c = 0
        while c in used: c += 1
        colors[u] = c
    return colors

if __name__ == "__main__":
    e = [(i, (i + 1) % 12) for i in range(12)]
    col = color_graph(12, e)
    assert all(col[u] != col[v] for u, v in e) and max(col) == 1
