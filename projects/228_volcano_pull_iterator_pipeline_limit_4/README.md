# 228 — Volcano Pull-Iterator Pipeline (Limit=4)

- **Track:** Database & Storage Internals
- **Complexity:** O(4) lazy tuples

## Overview
Demand-driven Scan -> Filter -> Project -> Limit SQL execution iterator (limit 4).

## Run & Verify
```bash
python3 main.py
```
