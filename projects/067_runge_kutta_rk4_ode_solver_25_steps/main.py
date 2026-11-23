import math

def rk4_decay(steps=25):
    h = 1.0 / steps; y = 1.0
    f = lambda val: -2.0 * val
    for _ in range(steps):
        k1 = f(y); k2 = f(y + 0.5 * h * k1); k3 = f(y + 0.5 * h * k2); k4 = f(y + h * k3)
        y += (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y

if __name__ == "__main__":
    assert abs(rk4_decay() - math.exp(-2.0)) < 1e-4
