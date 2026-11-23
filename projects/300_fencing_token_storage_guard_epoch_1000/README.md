# 300 — Fencing-Token Storage Guard (Epoch=1000)

- **Track:** Distributed Systems & Consensus
- **Complexity:** O(1) monotonicity

## Overview
Rejects zombie lease-holder writes carrying stale fencing tokens below epoch 1000.

## Run & Verify
```bash
python3 main.py
```
