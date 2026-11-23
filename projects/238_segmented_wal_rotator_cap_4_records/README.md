# 238 — Segmented WAL Rotator (Cap=4 Records)

- **Track:** Database & Storage Internals
- **Complexity:** O(1) append

## Overview
Rotates Write-Ahead Log segments every 4 entries and replays full state.

## Run & Verify
```bash
python3 main.py
```
