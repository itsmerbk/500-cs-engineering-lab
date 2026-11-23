class ChunkBitmap:
    def __init__(self): self.chunks = {}
    def add(self, x): self.chunks.setdefault(x >> 16, set()).add(x & 0xFFFF)
    def intersect(self, other):
        out = ChunkBitmap()
        for hi in set(self.chunks) & set(other.chunks):
            inter = self.chunks[hi] & other.chunks[hi]
            if inter: out.chunks[hi] = inter
        return out
    def card(self): return sum(len(s) for s in self.chunks.values())

if __name__ == "__main__":
    a, b = ChunkBitmap(), ChunkBitmap()
    for i in range(0, 5000, 2): a.add(i)
    for i in range(0, 5000, 4): b.add(i)
    assert a.intersect(b).card() == len(range(0, 5000, 4))
