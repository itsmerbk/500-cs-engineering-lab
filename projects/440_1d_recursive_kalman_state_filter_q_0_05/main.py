def kalman_1d(meas, q=0.05, r=0.1):
    x, p = meas[0], 1.0
    for z in meas[1:]:
        p += q
        k = p / (p + r)
        x += k * (z - x); p *= (1 - k)
    return x

if __name__ == "__main__":
    est = kalman_1d([10.2, 9.8, 10.1, 9.9, 10.0])
    assert abs(est - 10.0) < 0.2
