class FencedStorage:
    def __init__(self): self.max_tok, self.data = 0, None
    def write(self, tok, val):
        if tok < self.max_tok: return False
        self.max_tok, self.data = tok, val; return True

if __name__ == "__main__":
    st = FencedStorage()
    assert st.write(500, "new") and not st.write(500 - 1, "stale")
