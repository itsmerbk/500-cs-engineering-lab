def iir_step(p=0.4, steps=140):
    y = 0.0
    for _ in range(steps): y = 1.0 + p * y
    return y

if __name__ == "__main__":
    assert abs(iir_step() - (1.0 / (1.0 - 0.4))) < 1e-5
