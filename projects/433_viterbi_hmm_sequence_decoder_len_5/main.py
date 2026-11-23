def viterbi(obs):
    states = ["Sunny", "Rainy"]
    start = {"Sunny": 0.6, "Rainy": 0.4}
    trans = {"Sunny": {"Sunny": 0.8, "Rainy": 0.2}, "Rainy": {"Sunny": 0.3, "Rainy": 0.7}}
    emit = {"Sunny": {"walk": 0.7, "shop": 0.3}, "Rainy": {"walk": 0.2, "shop": 0.8}}
    dp = {s: (start[s] * emit[s][obs[0]], [s]) for s in states}
    for o in obs[1:]:
        dp = {s: max((dp[p][0]*trans[p][s]*emit[s][o], dp[p][1] + [s]) for p in states) for s in states}
    return max(dp.values())[1]

if __name__ == "__main__":
    path = viterbi(["walk"] * 5)
    assert path == ["Sunny"] * 5
