import random

class MultiLSH:
    def __init__(self, dim=8, tables=4, bits=4):
        rng = random.Random(42)
        self.proj = [[[rng.gauss(0, 1) for _ in range(dim)] for _ in range(bits)] for _ in range(tables)]
        self.buckets = [{} for _ in range(tables)]; self.vecs = {}
    def _h(self, t, v):
        return sum((1 << i) for i, p in enumerate(self.proj[t]) if sum(a*b for a, b in zip(v, p)) >= 0)
    def add(self, k, v):
        self.vecs[k] = v
        for t in range(len(self.proj)): self.buckets[t].setdefault(self._h(t, v), set()).add(k)
    def query(self, q):
        cands = set().union(*(self.buckets[t].get(self._h(t, q), set()) for t in range(len(self.proj)))) or set(self.vecs)
        return max(cands, key=lambda k: sum(a*b for a, b in zip(q, self.vecs[k])))

if __name__ == "__main__":
    idx = MultiLSH(); idx.add("target", [1.0]*8); idx.add("other", [-1.0]*8)
    assert idx.query([0.9]*8) == "target"
