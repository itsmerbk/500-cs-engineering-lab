# 298 — Fencing-Token Storage Guard (Epoch=100)

- **Track:** Distributed Systems & Consensus
- **Complexity:** O(1) monotonicity

## Overview
Rejects zombie lease-holder writes carrying stale fencing tokens below epoch 100.

## Run & Verify
```bash
python3 main.py
```
