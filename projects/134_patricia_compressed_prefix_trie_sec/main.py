class PrefixMap:
    def __init__(self): self.tree = {}
    def put(self, k, v):
        cur = self.tree
        for c in k: cur = cur.setdefault(c, {})
        cur["$"] = v
    def count_prefix(self, p):
        cur = self.tree
        for c in p:
            if c not in cur: return 0
            cur = cur[c]
        stack, cnt = [cur], 0
        while stack:
            n = stack.pop()
            if "$" in n: cnt += 1
            stack.extend(v for k, v in n.items() if k != "$")
        return cnt

if __name__ == "__main__":
    pm = PrefixMap()
    for i in range(6): pm.put(f"sec_node_{i}", i)
    pm.put("other_node", 99)
    assert pm.count_prefix("sec_") == 6
