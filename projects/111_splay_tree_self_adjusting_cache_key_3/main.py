class SNode:
    def __init__(self, k): self.k, self.l, self.r = k, None, None

def rot_r(x): y = x.l; x.l = y.r; y.r = x; return y
def rot_l(x): y = x.r; x.r = y.l; y.l = x; return y
def splay(root, k):
    if not root or root.k == k: return root
    if k < root.k:
        if not root.l: return root
        if k < root.l.k: root.l.l = splay(root.l.l, k); root = rot_r(root)
        elif k > root.l.k:
            root.l.r = splay(root.l.r, k)
            if root.l.r: root.l = rot_l(root.l)
        return rot_r(root) if root.l else root
    else:
        if not root.r: return root
        if k > root.r.k: root.r.r = splay(root.r.r, k); root = rot_l(root)
        elif k < root.r.k:
            root.r.l = splay(root.r.l, k)
            if root.r.l: root.r = rot_r(root.r)
        return rot_l(root) if root.r else root

if __name__ == "__main__":
    r = None
    for x in range(28):
        n = SNode(x); n.l = r; r = n
    r = splay(r, 3)
    assert r.k == 3
