def cla_add(a, b, bits=16):
    g = [(a >> i) & (b >> i) & 1 for i in range(bits)]
    p = [((a >> i) ^ (b >> i)) & 1 for i in range(bits)]
    c = [0] * (bits + 1)
    for i in range(bits): c[i + 1] = g[i] | (p[i] & c[i])
    return sum(((p[i] ^ c[i]) << i) for i in range(bits)), c[bits]

if __name__ == "__main__":
    hi = (1 << (16 - 1))
    assert cla_add(hi + 3, hi + 5) == (8, 1) and cla_add(5, 7) == (12, 0)
