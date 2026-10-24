from rsa_core import RSA, rsa_decrypt, rsa_encrypt

M = 100


if __name__ == "__main__":
    keys = RSA(bits=256)
    print(f"p = {keys.p}")
    print(f"q = {keys.q}")
    print(f"n = {keys.n}")
    print(f"Відкритий ключ (e, n): {keys.public_key}")
    print(f"Закритий ключ (d, n):  {keys.private_key}")

    C = rsa_encrypt(M, keys.e, keys.n)
    decrypted = rsa_decrypt(C, keys.d, keys.n)

    print(f"Відкритий текст M = {M}")
    print(f"Шифротекст C = {C}")
    print(f"Розшифрований текст = {decrypted}")
    print(f"Збіг: {decrypted == M}")
