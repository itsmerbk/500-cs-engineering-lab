# 226 — Volcano Pull-Iterator Pipeline (Limit=2)

- **Track:** Database & Storage Internals
- **Complexity:** O(2) lazy tuples

## Overview
Demand-driven Scan -> Filter -> Project -> Limit SQL execution iterator (limit 2).

## Run & Verify
```bash
python3 main.py
```
