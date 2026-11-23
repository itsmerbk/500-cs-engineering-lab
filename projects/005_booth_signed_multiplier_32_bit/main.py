def booth_mul(m, r, bits=32):
    mask = (1 << bits) - 1
    full_mask = (1 << (2 * bits + 1)) - 1
    sign_bit = 1 << (2 * bits)
    A = ((m & mask) << (bits + 1)) & full_mask
    S = (((-m) & mask) << (bits + 1)) & full_mask
    P = ((r & mask) << 1) & full_mask
    for _ in range(bits):
        op = P & 3
        if op == 1: P = (P + A) & full_mask
        elif op == 2: P = (P + S) & full_mask
        P = (P >> 1) | (P & sign_bit)
    res = (P >> 1) & ((1 << (2 * bits)) - 1)
    if res & (1 << (2 * bits - 1)): res -= 1 << (2 * bits)
    return res

if __name__ == "__main__":
    assert booth_mul(-13, 11) == -143 and booth_mul(-7, -9) == 63 and booth_mul(15, 12) == 180
