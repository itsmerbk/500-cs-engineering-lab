def rotl(v, n): return ((v << n) | (v >> (32 - n))) & 0xFFFFFFFF
def qr(s, a, b, c, d):
    s[a] = (s[a] + s[b]) & 0xFFFFFFFF; s[d] = rotl(s[d] ^ s[a], 16)
    s[c] = (s[c] + s[d]) & 0xFFFFFFFF; s[b] = rotl(s[b] ^ s[c], 12)
    s[a] = (s[a] + s[b]) & 0xFFFFFFFF; s[d] = rotl(s[d] ^ s[a], 8)
    s[c] = (s[c] + s[d]) & 0xFFFFFFFF; s[b] = rotl(s[b] ^ s[c], 7)

def chacha_xor(data, rounds=4):
    st = [0x61707865 + i for i in range(16)]
    for _ in range(rounds // 2): qr(st, 0, 4, 8, 12); qr(st, 1, 5, 9, 13)
    ks = b"".join(x.to_bytes(4, "little") for x in st)
    return bytes(b ^ ks[i % len(ks)] for i, b in enumerate(data))

if __name__ == "__main__":
    pt = b"zero-trust-channel"
    assert chacha_xor(chacha_xor(pt)) == pt
