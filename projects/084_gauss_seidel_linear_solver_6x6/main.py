def gauss_seidel(n=6, iters=45):
    A = [[float(n + 2 if i == j else 1) for j in range(n)] for i in range(n)]
    b = [sum(row) for row in A]
    x = [0.0] * n
    for _ in range(iters):
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i][i]
    return x

if __name__ == "__main__":
    assert max(abs(v - 1.0) for v in gauss_seidel()) < 1e-7
