# 249 — ARIES Redo/Undo Crash Recovery (5 Txns)

- **Track:** Database & Storage Internals
- **Complexity:** O(log) 3-pass

## Overview
Replays committed transactions and rolls back uncommitted updates across 5 transactions.

## Run & Verify
```bash
python3 main.py
```
