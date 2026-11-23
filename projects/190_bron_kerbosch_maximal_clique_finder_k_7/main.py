def max_clique(adj):
    best = []
    def bk(R, P, X):
        nonlocal best
        if not P and not X:
            if len(R) > len(best): best = list(R)
            return
        for v in list(P):
            bk(R | {v}, P & adj[v], X & adj[v])
            P.remove(v); X.add(v)
    bk(set(), set(adj), set())
    return best

if __name__ == "__main__":
    k = 7
    g = {i: set(range(k)) - {i} for i in range(k)}
    g[k] = {0}; g[0].add(k)
    assert len(max_clique(g)) == k
