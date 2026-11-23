import math

def erlang_c(traffic_erlangs, c=3):
    num = (traffic_erlangs ** c / math.factorial(c)) * (c / (c - traffic_erlangs))
    den = sum(traffic_erlangs ** k / math.factorial(k) for k in range(c)) + num
    return num / den

if __name__ == "__main__":
    pw = erlang_c(1.8)
    assert 0.0 < pw < 1.0
