def liveness(use, defn, succ):
    live_in, live_out = {}, {}
    for _ in range(len(use) + 1):
        for b in reversed(list(use)):
            lo = set().union(*(live_in.get(s, set()) for s in succ.get(b, [])))
            li = use[b] | (lo - defn[b])
            live_out[b], live_in[b] = lo, li
    return live_in

if __name__ == "__main__":
    li = liveness({"B1": {"x"}, "B2": {"y"}}, {"B1": {"y"}, "B2": set()}, {"B1": ["B2"]})
    assert li["B1"] == {"x"}
