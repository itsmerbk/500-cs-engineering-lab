import heapq

def prim_mst(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges: adj[u].append((w, v)); adj[v].append((w, u))
    vis = [False]*n; pq = [(0, 0)]; tot = cnt = 0
    while pq and cnt < n:
        w, u = heapq.heappop(pq)
        if vis[u]: continue
        vis[u] = True; tot += w; cnt += 1
        for nw, v in adj[u]:
            if not vis[v]: heapq.heappush(pq, (nw, v))
    return tot

if __name__ == "__main__":
    m = 1
    assert prim_mst(4, [(0,1,1*m),(0,2,4*m),(1,2,2*m),(1,3,3*m),(2,3,5*m)]) == 6 * m
