def bwt_roundtrip(s="COMPILER$"):
    rots = sorted(s[i:] + s[:i] for i in range(len(s)))
    last = "".join(r[-1] for r in rots)
    tbl = [""] * len(last)
    for _ in range(len(last)):
        tbl = sorted(last[i] + tbl[i] for i in range(len(last)))
    return next(row for row in tbl if row.endswith("$"))

if __name__ == "__main__":
    assert bwt_roundtrip() == "COMPILER$"
