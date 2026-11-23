def nth_root(val=2.0, d=5):
    x = 1.5
    for _ in range(30):
        x -= (x ** d - val) / (d * (x ** (d - 1)))
    return x

if __name__ == "__main__":
    r = nth_root()
    assert abs(r ** 5 - 2.0) < 1e-9
