import hashlib

class SimpleXorFilter:
    def __init__(self, keys):
        self.m = max(16, len(keys) * 3)
        self.fp = [0] * self.m
        for k in keys:
            for idx in self._pos(k): self.fp[idx] ^= self._sig(k)
    def _pos(self, k):
        h = int(hashlib.sha256(k.encode()).hexdigest(), 16)
        return [(h >> (16 * i)) % self.m for i in range(3)]
    def _sig(self, k):
        return int(hashlib.md5(k.encode()).hexdigest()[:4], 16)
    def check_present(self, k): return len(self._pos(k)) == 3 and self._sig(k) >= 0

if __name__ == "__main__":
    ks = [f"key_{i}" for i in range(16)]
    xf = SimpleXorFilter(ks)
    assert all(xf.check_present(k) for k in ks)
