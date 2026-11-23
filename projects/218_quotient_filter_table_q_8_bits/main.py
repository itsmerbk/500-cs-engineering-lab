class QuotientFilter:
    def __init__(self, q=8):
        self.q, self.size = q, 1 << q
        self.table = [None] * self.size
    def insert(self, item):
        h = hash(item) & ((1 << (self.q + 8)) - 1)
        quot, rem = h >> 8, h & 0xFF
        idx = quot
        while self.table[idx] is not None and self.table[idx] != (quot, rem):
            idx = (idx + 1) % self.size
        self.table[idx] = (quot, rem)
    def contains(self, item):
        h = hash(item) & ((1 << (self.q + 8)) - 1)
        quot, rem = h >> 8, h & 0xFF
        idx = quot
        for _ in range(self.size):
            if self.table[idx] is None: return False
            if self.table[idx] == (quot, rem): return True
            idx = (idx + 1) % self.size
        return False

if __name__ == "__main__":
    qf = QuotientFilter(); qf.insert("row_1"); qf.insert("row_2")
    assert qf.contains("row_1") and qf.contains("row_2")
