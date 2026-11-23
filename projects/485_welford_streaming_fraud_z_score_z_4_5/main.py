import math

class WelfordGuard:
    def __init__(self): self.n, self.mean, self.m2 = 0, 0.0, 0.0
    def observe(self, x):
        self.n += 1; d = x - self.mean; self.mean += d / self.n; self.m2 += d * (x - self.mean)
    def zscore(self, x):
        sd = math.sqrt(self.m2 / max(1, self.n - 1)) or 1.0
        return (x - self.mean) / sd

if __name__ == "__main__":
    wg = WelfordGuard()
    for v in [50.0, 52.0, 49.0, 51.0, 50.5, 49.5]: wg.observe(v)
    assert wg.zscore(500.0) > 4.5
