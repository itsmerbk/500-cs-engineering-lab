# 296 — Fencing-Token Storage Guard (Epoch=10)

- **Track:** Distributed Systems & Consensus
- **Complexity:** O(1) monotonicity

## Overview
Rejects zombie lease-holder writes carrying stale fencing tokens below epoch 10.

## Run & Verify
```bash
python3 main.py
```
