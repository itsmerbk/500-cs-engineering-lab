import math

def binomial_call(S=100.0, K=100.0, T=1.0, r=0.05, sigma=0.2, n=10):
    dt = T / n
    u = math.exp(sigma * math.sqrt(dt)); d = 1.0 / u
    p = (math.exp(r * dt) - d) / (u - d); disc = math.exp(-r * dt)
    vals = [max(0.0, S * (u ** (n - i)) * (d ** i) - K) for i in range(n + 1)]
    for step in range(n - 1, -1, -1):
        vals = [disc * (p * vals[i] + (1 - p) * vals[i + 1]) for i in range(step + 1)]
    return vals[0]

if __name__ == "__main__":
    assert 9.5 <= binomial_call() <= 11.5
