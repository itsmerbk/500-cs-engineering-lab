import itertools

def min_assignment(cost):
    n = len(cost)
    return min(sum(cost[i][p[i]] for i in range(n)) for p in itertools.permutations(range(n)))

if __name__ == "__main__":
    mat = [[1 if i == j else 10 for j in range(7)] for i in range(7)]
    assert min_assignment(mat) == 7
