class PNCounter:
    def __init__(self, n=4): self.p, self.n = [0]*n, [0]*n
    def inc(self, i, v=1): self.p[i] += v
    def dec(self, i, v=1): self.n[i] += v
    def merge(self, o):
        self.p = [max(a, b) for a, b in zip(self.p, o.p)]
        self.n = [max(a, b) for a, b in zip(self.n, o.n)]
    def value(self): return sum(self.p) - sum(self.n)

if __name__ == "__main__":
    r1, r2 = PNCounter(), PNCounter()
    r1.inc(0, 10); r2.dec(1, 3); r1.merge(r2); r2.merge(r1)
    assert r1.value() == r2.value() == 7
