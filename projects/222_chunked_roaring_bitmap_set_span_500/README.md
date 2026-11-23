# 222 — Chunked Roaring Bitmap Set (Span=500)

- **Track:** Database & Storage Internals
- **Complexity:** O(chunks) bitwise

## Overview
16-bit high-key partitioned compressed bitmap supporting fast set intersection (500).

## Run & Verify
```bash
python3 main.py
```
