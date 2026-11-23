def run_tape(code):
    tape, ptr, pc, out = [0]*32, 0, 0, []
    while pc < len(code):
        c = code[pc]
        if c == "+": tape[ptr] = (tape[ptr] + 1) & 255
        elif c == ".": out.append(chr(tape[ptr]))
        pc += 1
    return "".join(out)

if __name__ == "__main__":
    assert run_tape("+" * 68 + ".") == chr(68)
