def restoring_div(dividend, divisor, bits=32):
    rem = 0; quot = 0
    for i in range(bits - 1, -1, -1):
        rem = (rem << 1) | ((dividend >> i) & 1)
        if rem >= divisor:
            rem -= divisor; quot |= (1 << i)
    return quot, rem

if __name__ == "__main__":
    assert restoring_div(219, 13) == divmod(219, 13)
