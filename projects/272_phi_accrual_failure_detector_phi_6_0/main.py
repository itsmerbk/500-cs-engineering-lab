import math

def phi_suspicion(intervals, elapsed):
    mean = sum(intervals) / len(intervals)
    p = math.exp(-elapsed / mean)
    return -math.log10(max(p, 1e-12))

if __name__ == "__main__":
    assert phi_suspicion([10.0, 10.0, 10.0], 250.0) > 6.0
