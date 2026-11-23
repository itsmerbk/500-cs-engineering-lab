class HLC:
    def __init__(self): self.pt, self.l = 0, 0
    def send(self, wall):
        pt_new = max(self.pt, wall)
        self.l = (self.l + 1) if pt_new == self.pt else 0
        self.pt = pt_new; return (self.pt, self.l)
    def recv(self, wall, msg):
        pt_new = max(self.pt, msg[0], wall)
        if pt_new == self.pt == msg[0]: self.l = max(self.l, msg[1]) + 1
        elif pt_new == self.pt: self.l += 1
        elif pt_new == msg[0]: self.l = msg[1] + 1
        else: self.l = 0
        self.pt = pt_new; return (self.pt, self.l)

if __name__ == "__main__":
    a, b = HLC(), HLC()
    t1 = a.send(100 + 15); t2 = b.recv(100, t1)
    assert t2 > t1
