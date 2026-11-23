class INode:
    def __init__(self, lo, hi): self.lo, self.hi, self.max_hi, self.l, self.r = lo, hi, hi, None, None

def add_iv(n, lo, hi):
    if not n: return INode(lo, hi)
    if lo < n.lo: n.l = add_iv(n.l, lo, hi)
    else: n.r = add_iv(n.r, lo, hi)
    n.max_hi = max(n.max_hi, hi); return n

def query_iv(n, lo, hi, out):
    if not n: return
    if n.lo <= hi and lo <= n.hi: out.append((n.lo, n.hi))
    if n.l and n.l.max_hi >= lo: query_iv(n.l, lo, hi, out)
    query_iv(n.r, lo, hi, out)

if __name__ == "__main__":
    ivs = [(i * 4, i * 4 + 6) for i in range(12)]
    root = None
    for a, b in ivs: root = add_iv(root, a, b)
    got = []
    query_iv(root, 10, 12, got)
    exp = [x for x in ivs if x[0] <= 12 and 10 <= x[1]]
    assert sorted(got) == sorted(exp)
