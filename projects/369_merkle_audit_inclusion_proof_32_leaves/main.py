import hashlib

H = lambda x: hashlib.sha256(x).hexdigest()

def merkle_proof(items, idx):
    layer = [H(x.encode()) for x in items]; proof = []; pos = idx
    while len(layer) > 1:
        sib = pos ^ 1
        proof.append((sib < pos, layer[sib]))
        layer = [H((layer[i] + layer[i+1]).encode()) for i in range(0, len(layer), 2)]
        pos //= 2
    cur = H(items[idx].encode())
    for is_left, sh in proof:
        cur = H(((sh + cur) if is_left else (cur + sh)).encode())
    return cur == layer[0]

if __name__ == "__main__":
    assert merkle_proof([f"tx_{i}" for i in range(32)], 2)
