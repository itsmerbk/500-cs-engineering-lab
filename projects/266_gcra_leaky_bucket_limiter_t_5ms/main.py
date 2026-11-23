class GCRA:
    def __init__(self, interval=5, burst=2):
        self.T, self.tau, self.tat = interval, interval * burst, 0
    def allow(self, now):
        tat = max(self.tat, now)
        if tat - self.tau <= now:
            self.tat = tat + self.T; return True
        return False

if __name__ == "__main__":
    g = GCRA()
    assert g.allow(0) and g.allow(0) and g.allow(0) and not g.allow(0)
