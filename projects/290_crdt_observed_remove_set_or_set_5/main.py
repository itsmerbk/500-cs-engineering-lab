class ORSet:
    def __init__(self): self.adds, self.rems = set(), set()
    def add(self, elem, tag): self.adds.add((elem, tag))
    def remove(self, elem): self.rems |= {t for e, t in self.adds if e == elem}
    def merge(self, o): self.adds |= o.adds; self.rems |= o.rems
    def elements(self): return {e for e, t in self.adds if t not in self.rems}

if __name__ == "__main__":
    a, b = ORSet(), ORSet()
    a.add("item", "t1"); b.merge(a); b.remove("item"); a.add("item", "t2"); a.merge(b)
    assert "item" in a.elements()
