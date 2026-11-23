# 227 — Volcano Pull-Iterator Pipeline (Limit=3)

- **Track:** Database & Storage Internals
- **Complexity:** O(3) lazy tuples

## Overview
Demand-driven Scan -> Filter -> Project -> Limit SQL execution iterator (limit 3).

## Run & Verify
```bash
python3 main.py
```
