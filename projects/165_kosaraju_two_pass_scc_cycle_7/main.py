def kosaraju(n, edges):
    g = [[] for _ in range(n)]; rg = [[] for _ in range(n)]
    for u, v in edges: g[u].append(v); rg[v].append(u)
    vis, order = [False]*n, []
    def dfs1(u):
        vis[u] = True
        for v in g[u]:
            if not vis[v]: dfs1(v)
        order.append(u)
    for i in range(n):
        if not vis[i]: dfs1(i)
    vis = [False]*n; sccs = []
    def dfs2(u, comp):
        vis[u] = True; comp.append(u)
        for v in rg[u]:
            if not vis[v]: dfs2(v, comp)
    for u in reversed(order):
        if not vis[u]:
            c = []; dfs2(u, c); sccs.append(c)
    return sccs

if __name__ == "__main__":
    k = 7
    e = [(i, (i + 1) % k) for i in range(k)] + [(0, k)]
    assert len(kosaraju(k + 1, e)) == 2
