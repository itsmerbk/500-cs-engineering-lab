class SegmentedWAL:
    def __init__(self, cap=2): self.cap, self.segs = cap, [[]]
    def append(self, k, v):
        if len(self.segs[-1]) >= self.cap: self.segs.append([])
        self.segs[-1].append((k, v))
    def replay(self):
        st = {}
        for seg in self.segs:
            for k, v in seg: st[k] = v
        return st

if __name__ == "__main__":
    w = SegmentedWAL()
    for i in range(2 * 2 + 1): w.append(f"k{i}", i)
    assert len(w.segs) == 3 and len(w.replay()) == 2 * 2 + 1
