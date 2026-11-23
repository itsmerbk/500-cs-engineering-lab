import cmath, math

def dft(x):
    n = len(x)
    return [sum(x[t] * cmath.exp(-2j * math.pi * k * t / n) for t in range(n)) for k in range(n)]

if __name__ == "__main__":
    sig = [math.cos(2 * math.pi * 2 * t / 32) for t in range(32)]
    mags = [abs(v) for v in dft(sig)[:32//2]]
    assert mags.index(max(mags)) == 2
