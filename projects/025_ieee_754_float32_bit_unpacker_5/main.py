import struct

def unpack_f32(v):
    bits = struct.unpack(">I", struct.pack(">f", v))[0]
    sign = (bits >> 31) & 1
    exp = ((bits >> 23) & 0xFF) - 127
    mant = 1.0 + (bits & 0x7FFFFF) / (1 << 23)
    return ((-1) ** sign) * mant * (2.0 ** exp)

if __name__ == "__main__":
    assert abs(unpack_f32(-128.5) - (-128.5)) < 1e-5
