def compute_crc(data, poly=0x4c11db7, width=32):
    mask = (1 << width) - 1
    top = 1 << (width - 1)
    crc = mask
    for b in data:
        crc ^= (b << (width - 8))
        for _ in range(8):
            crc = (((crc << 1) ^ poly) if (crc & top) else (crc << 1)) & mask
    return crc

if __name__ == "__main__":
    assert compute_crc(b"SRM-COA") != compute_crc(b"SRM-COB")
