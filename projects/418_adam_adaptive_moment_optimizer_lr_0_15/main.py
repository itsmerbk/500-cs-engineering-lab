import math

def adam_minimize(lr=0.15, steps=300):
    x = 0.0; m = v = 0.0
    for t in range(1, steps + 1):
        g = 2.0 * (x - 4.0)
        m = 0.9 * m + 0.1 * g; v = 0.999 * v + 0.001 * g * g
        mh = m / (1 - 0.9 ** t); vh = v / (1 - 0.999 ** t)
        x -= lr * mh / (math.sqrt(vh) + 1e-8)
    return x

if __name__ == "__main__":
    assert abs(adam_minimize() - 4.0) < 1e-2
