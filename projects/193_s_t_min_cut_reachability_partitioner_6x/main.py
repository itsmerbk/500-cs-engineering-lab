from collections import deque

def min_cut_value(n, edges, s, t):
    cap = [[0]*n for _ in range(n)]
    for u, v, c in edges: cap[u][v] += c
    flow = 0
    while True:
        p = [-1]*n; p[s] = s; q = deque([s])
        while q and p[t] == -1:
            u = q.popleft()
            for v in range(n):
                if p[v] == -1 and cap[u][v] > 0: p[v] = u; q.append(v)
        if p[t] == -1: break
        f = 10**9; cur = t
        while cur != s: f = min(f, cap[p[cur]][cur]); cur = p[cur]
        cur = t
        while cur != s: cap[p[cur]][cur] -= f; cap[cur][p[cur]] += f; cur = p[cur]
        flow += f
    return flow

if __name__ == "__main__":
    assert min_cut_value(3, [(0, 1, 7 * 6), (1, 2, 4 * 6)], 0, 2) == 4 * 6
