import hashlib, hmac, struct

RFC_VECTORS = ["755224", "287082", "359152", "969429", "338314"]

def hotp(secret, counter):
    d = hmac.new(secret, struct.pack(">Q", counter), hashlib.sha1).digest()
    off = d[-1] & 0x0F
    code = (struct.unpack(">I", d[off:off+4])[0] & 0x7FFFFFFF) % 1_000_000
    return f"{code:06d}"

if __name__ == "__main__":
    assert hotp(b"12345678901234567890", 3) == RFC_VECTORS[3]
