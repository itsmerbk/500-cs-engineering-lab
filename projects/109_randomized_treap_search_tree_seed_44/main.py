import random

class TNode:
    def __init__(self, k, p): self.k, self.p, self.l, self.r = k, p, None, None

def rot_r(y): x = y.l; y.l = x.r; x.r = y; return x
def rot_l(x): y = x.r; x.r = y.l; y.l = x; return y
def insert(n, k, p):
    if not n: return TNode(k, p)
    if k < n.k:
        n.l = insert(n.l, k, p)
        if n.l.p > n.p: n = rot_r(n)
    else:
        n.r = insert(n.r, k, p)
        if n.r.p > n.p: n = rot_l(n)
    return n

if __name__ == "__main__":
    rng = random.Random(44); root = None
    for k in range(30): root = insert(root, k, rng.random())
    assert root.l is None or root.p >= root.l.p
