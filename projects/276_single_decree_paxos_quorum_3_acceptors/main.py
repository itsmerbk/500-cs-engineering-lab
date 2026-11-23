class Acceptor:
    def __init__(self): self.promised, self.accepted = -1, None
    def prepare(self, n):
        if n > self.promised: self.promised = n; return True, self.accepted
        return False, None
    def accept(self, n, v):
        if n >= self.promised: self.promised = n; self.accepted = (n, v); return True
        return False

if __name__ == "__main__":
    accs = [Acceptor() for _ in range(3)]
    if sum(1 for a in accs if a.prepare(1)[0]) > 3 // 2:
        ok = sum(1 for a in accs if a.accept(1, "COMMIT_X"))
        assert ok > 3 // 2
