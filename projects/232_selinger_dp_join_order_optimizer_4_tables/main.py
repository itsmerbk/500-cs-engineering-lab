def best_join_order(sizes):
    order = sorted(range(len(sizes)), key=lambda i: sizes[i])
    cost, cur = 0, sizes[order[0]]
    for idx in order[1:]:
        cur = max(1, (cur * sizes[idx]) // 10)
        cost += cur
    return order, cost

if __name__ == "__main__":
    sz = [1000 // (i + 1) for i in range(4)]
    ord_res, _ = best_join_order(sz)
    assert sz[ord_res[0]] <= sz[ord_res[-1]]
