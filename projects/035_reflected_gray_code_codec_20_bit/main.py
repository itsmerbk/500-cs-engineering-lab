def to_gray(n): return n ^ (n >> 1)
def from_gray(g):
    b = g
    while g > 0:
        g >>= 1; b ^= g
    return b

if __name__ == "__main__":
    for x in range(1 << min(20, 8)):
        assert from_gray(to_gray(x)) == x and bin(to_gray(x) ^ to_gray(x + 1)).count("1") == 1
