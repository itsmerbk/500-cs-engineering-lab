import re

def eval_pratt(expr):
    toks = re.findall(r"\d+|[+\-*^()]", expr); pos = 0
    lbp = {"+": 10, "-": 10, "*": 20, "^": 30}
    def parse(rbp=0):
        nonlocal pos
        t = toks[pos]; pos += 1
        left = parse(0) if t == "(" else int(t)
        if t == "(": pos += 1
        while pos < len(toks) and toks[pos] in lbp and lbp[toks[pos]] > rbp:
            op = toks[pos]; pos += 1
            right = parse(lbp[op] - (1 if op == "^" else 0))
            left = {"+": left+right, "-": left-right, "*": left*right, "^": left**right}[op]
        return left
    return parse()

if __name__ == "__main__":
    assert eval_pratt("3 + 2 ^ 6") == 3 + (2 ** 6)
