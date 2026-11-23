def kelly_fraction(p=0.7, odds=1.0):
    return max(0.0, (odds * p - (1.0 - p)) / odds)

if __name__ == "__main__":
    f = kelly_fraction()
    assert abs(f - (2 * 0.7 - 1)) < 1e-9
