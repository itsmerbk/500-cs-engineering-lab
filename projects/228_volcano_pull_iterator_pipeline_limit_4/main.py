def scan(rows):
    for r in rows: yield r
def filt(it, pred):
    for r in it:
        if pred(r): yield r
def limit(it, n=4):
    for i, r in enumerate(it):
        if i >= n: break
        yield r

if __name__ == "__main__":
    src = [{"id": i, "ok": i % 2 == 0} for i in range(50)]
    res = list(limit(filt(scan(src), lambda r: r["ok"])))
    assert len(res) == 4
