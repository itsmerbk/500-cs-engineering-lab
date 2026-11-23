def arith_roundtrip(bits, p0=0.85):
    lo, hi = 0.0, 1.0
    for b in bits:
        mid = lo + (hi - lo) * p0
        if b == 0: hi = mid
        else: lo = mid
    val = (lo + hi) / 2.0
    lo, hi, dec = 0.0, 1.0, []
    for _ in bits:
        mid = lo + (hi - lo) * p0
        if val < mid: dec.append(0); hi = mid
        else: dec.append(1); lo = mid
    return dec

if __name__ == "__main__":
    msg = [0, 0, 1, 0, 0, 0, 1, 0]
    assert arith_roundtrip(msg) == msg
