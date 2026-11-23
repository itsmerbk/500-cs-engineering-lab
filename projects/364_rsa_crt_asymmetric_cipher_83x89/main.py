def rsa_roundtrip(msg, p=83, q=89):
    n, phi, e = p * q, (p - 1) * (q - 1), 17
    d = pow(e, -1, phi)
    c = pow(msg, e, n)
    dp, dq, qinv = d % (p - 1), d % (q - 1), pow(q, -1, p)
    m1, m2 = pow(c, dp, p), pow(c, dq, q)
    h = (qinv * (m1 - m2)) % p
    return m2 + h * q

if __name__ == "__main__":
    assert rsa_roundtrip(420) == 420
