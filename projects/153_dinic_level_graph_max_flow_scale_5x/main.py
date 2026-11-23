from collections import deque

def dinic(n, edges, s, t):
    adj = [[] for _ in range(n)]
    for u, v, c in edges:
        adj[u].append([v, c, len(adj[v])]); adj[v].append([u, 0, len(adj[u]) - 1])
    flow = 0
    while True:
        lvl = [-1]*n; lvl[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for v, c, _ in adj[u]:
                if c > 0 and lvl[v] == -1: lvl[v] = lvl[u] + 1; q.append(v)
        if lvl[t] == -1: break
        ptr = [0]*n
        def dfs(u, pushed):
            if u == t or pushed == 0: return pushed
            while ptr[u] < len(adj[u]):
                v, c, rev = adj[u][ptr[u]]
                if lvl[v] == lvl[u] + 1 and c > 0:
                    tr = dfs(v, min(pushed, c))
                    if tr > 0:
                        adj[u][ptr[u]][1] -= tr; adj[v][rev][1] += tr; return tr
                ptr[u] += 1
            return 0
        while True:
            p = dfs(s, 10**9)
            if not p: break
            flow += p
    return flow

if __name__ == "__main__":
    s = 5
    assert dinic(4, [(0,1,10*s),(0,2,5*s),(1,2,15*s),(1,3,5*s),(2,3,10*s)], 0, 3) == 15 * s
