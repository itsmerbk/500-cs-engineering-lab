import math

def gram_schmidt(n=5):
    cols = [[1.0 if i <= j else 0.2 for i in range(n)] for j in range(n)]
    Q = []
    for v in cols:
        u = list(v)
        for q in Q:
            proj = sum(ui * qi for ui, qi in zip(u, q))
            u = [ui - proj * qi for ui, qi in zip(u, q)]
        norm = math.sqrt(sum(ui * ui for ui in u))
        Q.append([ui / norm for ui in u])
    return Q

if __name__ == "__main__":
    Q = gram_schmidt()
    for i in range(5):
        for j in range(5):
            dot = sum(a * b for a, b in zip(Q[i], Q[j]))
            assert abs(dot - (1.0 if i == j else 0.0)) < 1e-9
