def simpson(f, a, b, n=40):
    h = (b - a) / n
    s = f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, n))
    return s * h / 3.0

if __name__ == "__main__":
    assert abs(simpson(lambda x: 3 * x * x, 0.0, 2.0) - 8.0) < 1e-9
