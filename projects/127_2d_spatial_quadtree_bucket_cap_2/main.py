class QuadTree:
    def __init__(self, x, y, w, h, cap=2):
        self.box, self.cap, self.pts, self.kids = (x, y, w, h), cap, [], None
    def insert(self, pt):
        x, y, w, h = self.box
        if not (x <= pt[0] <= x + w and y <= pt[1] <= y + h): return False
        if len(self.pts) < self.cap and not self.kids:
            self.pts.append(pt); return True
        if not self.kids:
            hw, hh = w / 2, h / 2
            self.kids = [QuadTree(x, y, hw, hh, self.cap), QuadTree(x+hw, y, hw, hh, self.cap),
                         QuadTree(x, y+hh, hw, hh, self.cap), QuadTree(x+hw, y+hh, hw, hh, self.cap)]
        return any(k.insert(pt) for k in self.kids)
    def count(self):
        return len(self.pts) + (sum(k.count() for k in self.kids) if self.kids else 0)

if __name__ == "__main__":
    qt = QuadTree(0, 0, 100, 100)
    for i in range(12): qt.insert((i * 7.5, i * 6.0))
    assert qt.count() == 12
