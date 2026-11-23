import math

def norm_cdf(x): return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def bs_call_put(S=100.0, K=100.0, T=1.0, r=0.05, sigma=0.25):
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call = S * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    put = K * math.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)
    return call, put

if __name__ == "__main__":
    c, p = bs_call_put()
    assert abs((c - p) - (100.0 - 100.0 * math.exp(-0.05))) < 1e-7
