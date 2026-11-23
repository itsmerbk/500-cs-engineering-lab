def bounded_knapsack(items, cap=25):
    dp = [0] * (cap + 1)
    for w, v, cnt in items:
        for _ in range(cnt):
            for c in range(cap, w - 1, -1): dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]

if __name__ == "__main__":
    assert bounded_knapsack([(3, 25, 2), (4, 35, 2), (5, 50, 1)]) >= 70
