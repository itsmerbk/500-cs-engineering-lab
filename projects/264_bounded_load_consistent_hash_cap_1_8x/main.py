import math

def route_bounded(keys, nodes, factor=1.8):
    cap = math.ceil((len(keys) / len(nodes)) * factor)
    load = {n: 0 for n in nodes}; assign = {}
    for k in keys:
        start = hash(k) % len(nodes)
        for off in range(len(nodes)):
            cand = nodes[(start + off) % len(nodes)]
            if load[cand] < cap: load[cand] += 1; assign[k] = cand; break
    return load

if __name__ == "__main__":
    ld = route_bounded([f"k{i}" for i in range(20)], ["n1", "n2", "n3"])
    assert max(ld.values()) <= math.ceil((20 / 3) * 1.8)
