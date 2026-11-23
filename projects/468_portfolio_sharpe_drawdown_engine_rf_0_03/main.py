import math

def risk_metrics(rets, rf_step=0.03/252):
    ex = [r - rf_step for r in rets]
    mu = sum(ex) / len(ex)
    sd = math.sqrt(sum((x - mu)**2 for x in ex) / len(ex))
    eq, peak, mdd = 1.0, 1.0, 0.0
    for r in rets:
        eq *= (1 + r); peak = max(peak, eq); mdd = max(mdd, (peak - eq) / peak)
    return (mu / sd) * math.sqrt(252), mdd

if __name__ == "__main__":
    sh, dd = risk_metrics([0.01, -0.005, 0.012, 0.008, -0.003])
    assert sh > 0 and 0 < dd < 0.02
