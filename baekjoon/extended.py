def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # 역원이 존재하지 않음
    else:
        return x % m

result = find_inverse(17, 1009)
print(result)
