def compute_first(rules):
    first = {nt: set() for nt in rules}
    changed = True
    while changed:
        changed = False
        for nt, prods in rules.items():
            for p in prods:
                sym = p[0]
                add = first[sym] if sym in rules else {sym}
                if not add.issubset(first[nt]): first[nt] |= add; changed = True
    return first

if __name__ == "__main__":
    f = compute_first({"S": ["A", "b"], "A": ["a", "c"]})
    assert f["S"] == {"a", "b", "c"}
