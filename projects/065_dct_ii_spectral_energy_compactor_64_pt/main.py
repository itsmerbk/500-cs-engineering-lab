import math

def dct2(x):
    n = len(x)
    return [sum(x[i] * math.cos(math.pi * k * (2 * i + 1) / (2 * n)) for i in range(n)) for k in range(n)]

if __name__ == "__main__":
    c = dct2([i / 64 for i in range(64)])
    tot = sum(v * v for v in c)
    assert sum(v * v for v in c[:3]) / tot > 0.95
