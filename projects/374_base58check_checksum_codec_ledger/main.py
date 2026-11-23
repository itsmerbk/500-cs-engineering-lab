import hashlib

ALPH = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def b58check_roundtrip(raw=b'ledger-tx'):
    chk = hashlib.sha256(hashlib.sha256(raw).digest()).digest()[:4]
    num = int.from_bytes(raw + chk, "big"); enc = ""
    while num > 0: num, rem = divmod(num, 58); enc = ALPH[rem] + enc
    val = 0
    for c in enc: val = val * 58 + ALPH.index(c)
    dec = val.to_bytes(len(raw) + 4, "big")
    assert dec[-4:] == hashlib.sha256(hashlib.sha256(dec[:-4]).digest()).digest()[:4]
    return dec[:-4]

if __name__ == "__main__":
    assert b58check_roundtrip() == b'ledger-tx'
