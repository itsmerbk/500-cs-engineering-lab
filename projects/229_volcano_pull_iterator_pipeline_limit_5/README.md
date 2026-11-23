# 229 — Volcano Pull-Iterator Pipeline (Limit=5)

- **Track:** Database & Storage Internals
- **Complexity:** O(5) lazy tuples

## Overview
Demand-driven Scan -> Filter -> Project -> Limit SQL execution iterator (limit 5).

## Run & Verify
```bash
python3 main.py
```
