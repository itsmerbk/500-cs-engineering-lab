class CuckooMap:
    def __init__(self, m=29): self.m, self.t1, self.t2 = m, [None]*m, [None]*m
    def _h1(self, k): return (k * 2654435761) % self.m
    def _h2(self, k): return (k * 40503 + 7) % self.m
    def put(self, k, v):
        cur = (k, v)
        for _ in range(64):
            i1 = self._h1(cur[0])
            if self.t1[i1] is None or self.t1[i1][0] == cur[0]: self.t1[i1] = cur; return
            cur, self.t1[i1] = self.t1[i1], cur
            i2 = self._h2(cur[0])
            if self.t2[i2] is None or self.t2[i2][0] == cur[0]: self.t2[i2] = cur; return
            cur, self.t2[i2] = self.t2[i2], cur
    def get(self, k):
        for idx, tbl in [(self._h1(k), self.t1), (self._h2(k), self.t2)]:
            if tbl[idx] and tbl[idx][0] == k: return tbl[idx][1]
        return None

if __name__ == "__main__":
    cm = CuckooMap()
    for i in range(29 // 2): cm.put(i * 3, i * 10)
    assert all(cm.get(i * 3) == i * 10 for i in range(29 // 2))
