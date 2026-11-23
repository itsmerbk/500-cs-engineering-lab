import cmath, math

def dft_idft_err(sig):
    n = len(sig)
    X = [sum(sig[t] * cmath.exp(-2j * math.pi * k * t / n) for t in range(n)) for k in range(n)]
    rec = [sum(X[k] * cmath.exp(2j * math.pi * k * t / n) for k in range(n)).real / n for t in range(n)]
    return max(abs(a - b) for a, b in zip(sig, rec))

if __name__ == "__main__":
    assert dft_idft_err([float((i * 3) % 7) for i in range(48)]) < 1e-9
