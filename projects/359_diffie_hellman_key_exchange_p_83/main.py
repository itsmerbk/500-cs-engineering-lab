def dh_shared(p=83, g=5, a=6, b=15):
    A, B = pow(g, a, p), pow(g, b, p)
    return pow(B, a, p), pow(A, b, p)

if __name__ == "__main__":
    s1, s2 = dh_shared()
    assert s1 == s2
