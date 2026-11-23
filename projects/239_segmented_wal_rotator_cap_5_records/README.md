# 239 — Segmented WAL Rotator (Cap=5 Records)

- **Track:** Database & Storage Internals
- **Complexity:** O(1) append

## Overview
Rotates Write-Ahead Log segments every 5 entries and replays full state.

## Run & Verify
```bash
python3 main.py
```
