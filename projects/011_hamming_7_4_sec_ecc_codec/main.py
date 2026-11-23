def hamming_roundtrip(data_bits, r=3):
    n = (1 << r) - 1
    cw = [0] * (n + 1)
    di = 0
    for pos in range(1, n + 1):
        if pos & (pos - 1):
            cw[pos] = data_bits[di]; di += 1
    for j in range(r):
        p = 1 << j
        cw[p] = sum(cw[pos] for pos in range(1, n + 1) if pos & p) & 1
    corrupted = list(cw)
    corrupted[3] ^= 1
    syn = sum((1 << j) for j in range(r) if (sum(corrupted[pos] for pos in range(1, n + 1) if pos & (1 << j)) & 1))
    if syn: corrupted[syn] ^= 1
    return [corrupted[pos] for pos in range(1, n + 1) if pos & (pos - 1)]

if __name__ == "__main__":
    bits = [(i * 7 + 1) & 1 for i in range(4)]
    assert hamming_roundtrip(bits) == bits
