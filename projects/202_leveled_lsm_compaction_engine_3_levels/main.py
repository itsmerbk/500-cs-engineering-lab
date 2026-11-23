def compact_levels(levels):
    merged = {}
    for lvl in reversed(levels):
        for k, v in lvl.items(): merged[k] = v
    return {k: v for k, v in merged.items() if v is not None}

if __name__ == "__main__":
    lv = [{"k1": "new", "k2": None} if i == 0 else {"k1": "old", "k2": "v2", f"x{i}": i} for i in range(3)]
    res = compact_levels(lv)
    assert res["k1"] == "new" and "k2" not in res
