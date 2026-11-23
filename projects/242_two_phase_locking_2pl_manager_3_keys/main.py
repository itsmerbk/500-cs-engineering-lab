class LockManager:
    def __init__(self): self.locks = {}
    def lock_x(self, tx, key):
        holder = self.locks.get(key)
        if holder in (None, tx): self.locks[key] = tx; return True
        return False
    def release_all(self, tx):
        self.locks = {k: v for k, v in self.locks.items() if v != tx}

if __name__ == "__main__":
    lm = LockManager()
    assert lm.lock_x("T1", "r0") and not lm.lock_x("T2", "r0")
    lm.release_all("T1"); assert lm.lock_x("T2", "r0")
