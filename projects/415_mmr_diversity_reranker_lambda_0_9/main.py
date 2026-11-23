def mmr_select(rel, sim, k=2, lam=0.9):
    sel = [max(rel, key=rel.get)]
    while len(sel) < k:
        cand = max((d for d in rel if d not in sel),
                   key=lambda d: lam * rel[d] - (1 - lam) * max(sim[(d, s)] for s in sel))
        sel.append(cand)
    return sel

if __name__ == "__main__":
    rel = {"d1": 0.95, "d2": 0.94, "d3": 0.80}
    sim = {("d2","d1"): 0.99, ("d3","d1"): 0.10}
    assert mmr_select(rel, sim)[0] == "d1"
