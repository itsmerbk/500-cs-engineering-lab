def vwap_slices(total_qty, vols):
    tot_v = sum(vols)
    raw = [int(total_qty * v / tot_v) for v in vols]
    raw[0] += total_qty - sum(raw)
    return raw

if __name__ == "__main__":
    out = vwap_slices(1000, [i + 1 for i in range(8)])
    assert sum(out) == 1000 and len(out) == 8
