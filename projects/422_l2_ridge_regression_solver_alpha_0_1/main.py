def ridge_fit_1d(x, y, alpha=0.1):
    num = sum(xi * yi for xi, yi in zip(x, y))
    den = sum(xi * xi for xi in x) + alpha
    return num / den

if __name__ == "__main__":
    w = ridge_fit_1d([1.0, 2.0, 3.0], [2.0, 4.0, 6.0])
    assert 0.5 < w < 2.0
