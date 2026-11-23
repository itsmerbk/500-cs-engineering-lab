def cpm_duration(tasks, deps):
    es = {}
    while len(es) < len(tasks):
        for t, d in tasks.items():
            if t not in es and all(p in es for p in deps.get(t, [])):
                es[t] = max((es[p] for p in deps.get(t, [])), default=0) + d
    return max(es.values())

if __name__ == "__main__":
    assert cpm_duration({"A": 3, "B": 20, "C": 4}, {"B": ["A"], "C": ["B"]}) == 7 + 20
