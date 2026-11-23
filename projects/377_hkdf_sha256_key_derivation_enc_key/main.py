import hashlib, hmac

def hkdf_sha256(ikm, salt=b"salt", info=b'enc-key', length=32):
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()
    return hmac.new(prk, info + b"\x01", hashlib.sha256).digest()[:length]

if __name__ == "__main__":
    k1 = hkdf_sha256(b"master-secret")
    assert len(k1) == 32 and k1 != hkdf_sha256(b"other-secret")
