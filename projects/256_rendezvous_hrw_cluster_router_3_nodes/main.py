import hashlib

def hrw_pick(key, nodes):
    return max(nodes, key=lambda n: hashlib.sha256(f"{n}:{key}".encode()).hexdigest())

if __name__ == "__main__":
    ns = [f"shard-{i}" for i in range(3)]
    picked = hrw_pick("acct:99", ns)
    rem = [n for n in ns if n != picked]
    assert hrw_pick("acct:99", rem) in rem
