class FXLedger:
    def __init__(self, usd_inr=83.0): self.rate, self.entries = usd_inr, []
    def post_fx(self, usd_amt):
        inr = round(usd_amt * self.rate, 2)
        self.entries.append(("USD_CASH", inr)); self.entries.append(("INR_SETTLE", -inr))
    def balanced(self): return round(sum(v for _, v in self.entries), 2) == 0.0

if __name__ == "__main__":
    lg = FXLedger(); lg.post_fx(250.0)
    assert lg.balanced()
