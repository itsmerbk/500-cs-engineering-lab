def run_saga(n_steps, fail_idx=3):
    done = []
    for i in range(1, n_steps + 1):
        if i == fail_idx: return ["UNDO_" + s for s in reversed(done)]
        done.append(f"STEP_{i}")
    return done

if __name__ == "__main__":
    res = run_saga(6)
    assert len(res) == 3 - 1 and all(x.startswith("UNDO_") for x in res)
