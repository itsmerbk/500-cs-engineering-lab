import math

def tour_len(pts, t):
    return sum(math.hypot(pts[t[i]][0]-pts[t[(i+1)%len(t)]][0], pts[t[i]][1]-pts[t[(i+1)%len(t)]][1]) for i in range(len(t)))

def two_opt(pts):
    t = list(range(len(pts))); improved = True
    while improved:
        improved = False
        for i in range(1, len(t) - 1):
            for j in range(i + 1, len(t)):
                nt = t[:i] + t[i:j+1][::-1] + t[j+1:]
                if tour_len(pts, nt) + 1e-9 < tour_len(pts, t): t = nt; improved = True
    return t

if __name__ == "__main__":
    pts = [(math.cos(2*math.pi*i/14), math.sin(2*math.pi*i/14)) for i in range(14)]
    init = list(range(14)); init[1], init[3] = init[3], init[1]
    opt = two_opt(pts)
    assert tour_len(pts, opt) <= tour_len(pts, init) and len(set(opt)) == 14
