import ipaddress

def eval_acl(rules, src_ip, port):
    ip = ipaddress.ip_address(src_ip)
    for action, cidr, p in rules:
        if ip in ipaddress.ip_network(cidr) and p in (port, "*"): return action
    return "DENY"

if __name__ == "__main__":
    r = [("DENY", "10.0.99.0/24", "*"), ("ALLOW", "10.0.0.0/8", 80)]
    assert eval_acl(r, "10.0.1.5", 80) == "ALLOW" and eval_acl(r, "10.0.99.5", 80) == "DENY"
