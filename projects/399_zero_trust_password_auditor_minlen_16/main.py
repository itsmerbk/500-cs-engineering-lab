def audit_pw(pw, blocklist={"Password123!", "Admin@2026"}):
    if pw in blocklist or len(pw) < 16: return False
    classes = sum([any(c.islower() for c in pw), any(c.isupper() for c in pw),
                   any(c.isdigit() for c in pw), any(not c.isalnum() for c in pw)])
    return classes >= 3

if __name__ == "__main__":
    assert audit_pw("SrmCse#2029_SecurePass") and not audit_pw("short1A!")
