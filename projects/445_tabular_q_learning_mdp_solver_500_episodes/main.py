def train_q(episodes=500):
    Q = [[0.0, 0.0] for _ in range(4)]
    for _ in range(episodes):
        s = 0
        while s < 3:
            ns = s + 1
            r = 10.0 if ns == 3 else -0.1
            Q[s][1] += 0.2 * (r + 0.9 * max(Q[ns]) - Q[s][1])
            s = ns
    return Q

if __name__ == "__main__":
    q = train_q()
    assert q[0][1] > q[0][0]
