class N:
    def __init__(self, k): self.k, self.l, self.r, self.h = k, None, None, 1

def ht(n): return n.h if n else 0
def rot_r(y):
    x = y.l; y.l = x.r; x.r = y
    y.h = 1 + max(ht(y.l), ht(y.r)); x.h = 1 + max(ht(x.l), ht(x.r)); return x
def rot_l(x):
    y = x.r; x.r = y.l; y.l = x
    x.h = 1 + max(ht(x.l), ht(x.r)); y.h = 1 + max(ht(y.l), ht(y.r)); return y
def ins(n, k):
    if not n: return N(k)
    if k < n.k: n.l = ins(n.l, k)
    else: n.r = ins(n.r, k)
    n.h = 1 + max(ht(n.l), ht(n.r))
    b = ht(n.l) - ht(n.r)
    if b > 1 and k < n.l.k: return rot_r(n)
    if b < -1 and k > n.r.k: return rot_l(n)
    if b > 1 and k > n.l.k: n.l = rot_l(n.l); return rot_r(n)
    if b < -1 and k < n.r.k: n.r = rot_r(n.r); return rot_l(n)
    return n

if __name__ == "__main__":
    root = None
    for x in range(31): root = ins(root, x)
    assert root.h <= 12
