import math, random

def train_xor(seed=14):
    rng = random.Random(seed)
    W1 = [[rng.uniform(-1, 1) for _ in range(2)] for _ in range(3)]
    W2 = [rng.uniform(-1, 1) for _ in range(3)]
    data = [([0,0], 0), ([0,1], 1), ([1,0], 1), ([1,1], 0)]
    for _ in range(3500):
        for x, y in data:
            h = [math.tanh(sum(W1[j][i]*x[i] for i in range(2))) for j in range(3)]
            out = 1 / (1 + math.exp(-sum(W2[j]*h[j] for j in range(3))))
            err = out - y
            for j in range(3):
                g_h = err * W2[j] * (1 - h[j]**2)
                W2[j] -= 0.2 * err * h[j]
                for i in range(2): W1[j][i] -= 0.2 * g_h * x[i]
    preds = [round(1 / (1 + math.exp(-sum(W2[j]*math.tanh(sum(W1[j][i]*x[i] for i in range(2))) for j in range(3))))) for x, _ in data]
    return preds

if __name__ == "__main__":
    assert train_xor() == [0, 1, 1, 0]
