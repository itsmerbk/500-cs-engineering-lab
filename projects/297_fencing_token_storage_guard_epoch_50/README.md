# 297 — Fencing-Token Storage Guard (Epoch=50)

- **Track:** Distributed Systems & Consensus
- **Complexity:** O(1) monotonicity

## Overview
Rejects zombie lease-holder writes carrying stale fencing tokens below epoch 50.

## Run & Verify
```bash
python3 main.py
```
