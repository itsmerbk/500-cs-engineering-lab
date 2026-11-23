def euler_circuit(n, edges):
    adj = [list() for _ in range(n)]
    for idx, (u, v) in enumerate(edges): adj[u].append((v, idx)); adj[v].append((u, idx))
    used = [False]*len(edges); st = [0]; path = []
    while st:
        u = st[-1]
        while adj[u] and used[adj[u][-1][1]]: adj[u].pop()
        if adj[u]:
            v, eid = adj[u].pop(); used[eid] = True; st.append(v)
        else: path.append(st.pop())
    return path[::-1]

if __name__ == "__main__":
    k = 7
    e = [(i, (i + 1) % k) for i in range(k)]
    p = euler_circuit(k, e)
    assert len(p) == k + 1 and p[0] == p[-1]
