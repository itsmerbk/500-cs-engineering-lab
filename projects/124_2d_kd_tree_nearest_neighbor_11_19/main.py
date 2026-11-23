def build_kd(pts, d=0):
    if not pts: return None
    pts = sorted(pts, key=lambda p: p[d % 2])
    m = len(pts) // 2
    return (pts[m], build_kd(pts[:m], d + 1), build_kd(pts[m + 1:], d + 1))

def nn(node, target, d=0, best=None):
    if not node: return best
    pt, l, r = node
    dist = (pt[0] - target[0])**2 + (pt[1] - target[1])**2
    if best is None or dist < best[0]: best = (dist, pt)
    axis = d % 2
    diff = target[axis] - pt[axis]
    near, far = (l, r) if diff < 0 else (r, l)
    best = nn(near, target, d + 1, best)
    if diff * diff < best[0]: best = nn(far, target, d + 1, best)
    return best

if __name__ == "__main__":
    pts = [(i * 3, (i * 7) % 23) for i in range(15)]
    t = (11, 19)
    assert nn(build_kd(pts), t)[0] == min((p[0]-t[0])**2 + (p[1]-t[1])**2 for p in pts)
