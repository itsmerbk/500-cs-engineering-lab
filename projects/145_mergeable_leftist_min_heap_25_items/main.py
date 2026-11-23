class LNode:
    def __init__(self, k): self.k, self.l, self.r, self.s = k, None, None, 1

def meld(a, b):
    if not a or not b: return a or b
    if a.k > b.k: a, b = b, a
    a.r = meld(a.r, b)
    sl = a.l.s if a.l else 0
    sr = a.r.s if a.r else 0
    if sl < sr: a.l, a.r = a.r, a.l
    a.s = (a.r.s if a.r else 0) + 1
    return a

if __name__ == "__main__":
    h1 = h2 = None
    for x in range(0, 25, 2): h1 = meld(h1, LNode(x))
    for x in range(1, 25, 2): h2 = meld(h2, LNode(x))
    merged = meld(h1, h2)
    out = []
    while merged: out.append(merged.k); merged = meld(merged.l, merged.r)
    assert out == list(range(25))
