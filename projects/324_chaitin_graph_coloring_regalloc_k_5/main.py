def alloc_regs(adj, k=5):
    stack, g = [], {u: set(vs) for u, vs in adj.items()}
    while g:
        u = min(g, key=lambda x: len(g[x]))
        stack.append(u)
        for v in g[u]: g[v].discard(u)
        del g[u]
    reg = {}
    while stack:
        u = stack.pop()
        used = {reg[v] for v in adj[u] if v in reg}
        reg[u] = next(r for r in range(k) if r not in used)
    return reg

if __name__ == "__main__":
    r = alloc_regs({"a": {"b"}, "b": {"a"}})
    assert r["a"] != r["b"]
