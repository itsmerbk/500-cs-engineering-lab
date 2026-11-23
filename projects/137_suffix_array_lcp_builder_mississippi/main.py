def build_sa_lcp(s="mississippi$"):
    sa = sorted(range(len(s)), key=lambda i: s[i:])
    lcp = [0] * len(s)
    for i in range(1, len(s)):
        a, b, k = sa[i - 1], sa[i], 0
        while a + k < len(s) and b + k < len(s) and s[a + k] == s[b + k]: k += 1
        lcp[i] = k
    return sa, lcp

if __name__ == "__main__":
    sa, lcp = build_sa_lcp()
    assert len(sa) == len("mississippi$") and max(lcp) >= 1
