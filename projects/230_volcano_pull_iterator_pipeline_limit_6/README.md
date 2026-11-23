# 230 — Volcano Pull-Iterator Pipeline (Limit=6)

- **Track:** Database & Storage Internals
- **Complexity:** O(6) lazy tuples

## Overview
Demand-driven Scan -> Filter -> Project -> Limit SQL execution iterator (limit 6).

## Run & Verify
```bash
python3 main.py
```
