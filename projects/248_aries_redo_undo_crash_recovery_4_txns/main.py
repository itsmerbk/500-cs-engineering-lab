def aries_recover(records):
    committed = {r[1] for r in records if r[0] == "COMMIT"}
    state = {}
    for op, tx, k, val in records:
        if op == "WRITE" and tx in committed: state[k] = val
    return state

if __name__ == "__main__":
    log = [("WRITE", "T1", "a", 10), ("COMMIT", "T1", "", 0), ("WRITE", "T2", "a", 99)]
    assert aries_recover(log)["a"] == 10
