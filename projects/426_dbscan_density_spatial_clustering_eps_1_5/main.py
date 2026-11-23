def dbscan(pts, eps=1.5, min_pts=2):
    labels = [-1]*len(pts); cid = 0
    def nb(i): return [j for j, p in enumerate(pts) if (pts[i][0]-p[0])**2 + (pts[i][1]-p[1])**2 <= eps*eps]
    for i in range(len(pts)):
        if labels[i] != -1: continue
        ns = nb(i)
        if len(ns) < min_pts: continue
        labels[i] = cid; q = list(ns)
        while q:
            j = q.pop()
            if labels[j] == -1:
                labels[j] = cid; n2 = nb(j)
                if len(n2) >= min_pts: q.extend(n2)
        cid += 1
    return labels

if __name__ == "__main__":
    res = dbscan([(0,0), (0,1), (10,10), (10,11), (50,50)])
    assert res[0] == res[1] and res[2] == res[3] and res[4] == -1
