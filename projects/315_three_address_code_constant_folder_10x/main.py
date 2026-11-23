def fold_tac(ir):
    consts, out = {}, []
    for dst, op, a, b in ir:
        va = consts.get(a, a); vb = consts.get(b, b)
        if isinstance(va, int) and isinstance(vb, int):
            val = va + vb if op == "+" else va * vb
            consts[dst] = val; out.append((dst, "CONST", val, None))
        else: out.append((dst, op, va, vb))
    return out

if __name__ == "__main__":
    opt = fold_tac([("t1", "+", 3, 4), ("t2", "*", "t1", 10)])
    assert opt[-1] == ("t2", "CONST", 7 * 10, None)
