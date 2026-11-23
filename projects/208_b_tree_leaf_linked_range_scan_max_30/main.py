class BPlusLeaf:
    def __init__(self, pairs): self.pairs = sorted(pairs)
    def scan(self, lo, hi): return [(k, v) for k, v in self.pairs if lo <= k <= hi]

if __name__ == "__main__":
    bp = BPlusLeaf([(i * 2, f"v{i}") for i in range(30)])
    rows = bp.scan(5, 30)
    assert all(5 <= k <= 30 for k, _ in rows)
