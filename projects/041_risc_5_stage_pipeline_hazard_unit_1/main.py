def count_stalls(insts, forwarding=True):
    stalls = 0
    for i in range(1, len(insts)):
        prev_dst = insts[i - 1][1]
        if prev_dst in (insts[i][2], insts[i][3]):
            stalls += 1 if forwarding else 2
    return stalls

if __name__ == "__main__":
    prog = [("ADD", "R1", "R2", "R3"), ("SUB", "R4", "R1", "R5"), ("MUL", "R6", "R4", "R1")]
    assert count_stalls(prog, False) > count_stalls(prog, True)
