def convolve1d(sig, ker):
    n, m = len(sig), len(ker)
    out = [0.0] * (n + m - 1)
    for i, sv in enumerate(sig):
        for j, kv in enumerate(ker): out[i + j] += sv * kv
    return out

if __name__ == "__main__":
    res = convolve1d([0.0, 0.0, 1.0, 0.0, 0.0], [1.0 / 7] * 7)
    assert abs(sum(res) - 1.0) < 1e-9
