def lfsr_seq(seed, steps=15, poly=0xe08):
    st = seed; out = []
    for _ in range(steps):
        out.append(st)
        lsb = st & 1; st >>= 1
        if lsb: st ^= poly
    return out

if __name__ == "__main__":
    assert len(set(lfsr_seq(1, 15))) == 15
