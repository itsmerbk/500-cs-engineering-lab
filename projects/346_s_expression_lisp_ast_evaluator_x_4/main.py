def eval_sexpr(node):
    if isinstance(node, int): return node
    op, args = node[0], [eval_sexpr(a) for a in node[1:]]
    return sum(args) if op == "+" else args[0] * args[1]

if __name__ == "__main__":
    assert eval_sexpr(["+", ["*", 4, 3], 5]) == 4 * 3 + 5
