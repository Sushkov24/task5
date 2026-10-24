import math
import random

_rng = random.SystemRandom()
PUBLIC_EXPONENT = 65537
_SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(n: int, rounds: int = 40) -> bool:
    if n < 2:
        return False
    for p in _SMALL_PRIMES:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(rounds):
        a = _rng.randrange(2, n - 1)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime(bits: int) -> int:
    while True:
        candidate = _rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_prime(candidate):
            return candidate


class RSA:
    def __init__(self, bits: int = 512, e: int = PUBLIC_EXPONENT):
        while True:
            self.p = generate_prime(bits)
            self.q = generate_prime(bits)
            phi = (self.p - 1) * (self.q - 1)
            if self.p != self.q and math.gcd(e, phi) == 1:
                break
        self.n = self.p * self.q
        self.e = e
        self.d = pow(e, -1, phi)

    @property
    def public_key(self) -> tuple[int, int]:
        return self.e, self.n

    @property
    def private_key(self) -> tuple[int, int]:
        return self.d, self.n


def rsa_encrypt(m: int, e: int, n: int) -> int:
    if not 0 <= m < n:
        raise ValueError("повідомлення має бути в діапазоні [0, n)")
    return pow(m, e, n)


def rsa_decrypt(c: int, d: int, n: int) -> int:
    return pow(c, d, n)
