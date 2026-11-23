import hashlib

def sign_manifest(files):
    return {k: hashlib.sha256(v).hexdigest() for k, v in files.items()}

if __name__ == "__main__":
    orig = {f"f{i}.bin": f"data_{i}".encode() for i in range(7)}
    m = sign_manifest(orig)
    tampered = dict(orig); tampered["f0.bin"] = b"evil"
    assert [k for k, h in sign_manifest(tampered).items() if h != m[k]] == ["f0.bin"]
