def mtf_roundtrip(s="mississippi"):
    alpha = [chr(i) for i in range(256)]; codes = []
    for c in s:
        idx = alpha.index(c); codes.append(idx); alpha.pop(idx); alpha.insert(0, c)
    alpha = [chr(i) for i in range(256)]; out = []
    for idx in codes:
        c = alpha[idx]; out.append(c); alpha.pop(idx); alpha.insert(0, c)
    return "".join(out)

if __name__ == "__main__":
    assert mtf_roundtrip() == "mississippi"
