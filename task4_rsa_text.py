import base64

from rsa_core import RSA, rsa_decrypt, rsa_encrypt

TEST_TEXT = (
    "Cryptography is fun and educational! Learning RSA encryption and "
    "decryption with Python helps understand public key cryptosystems."
)
UKR_TEXT = "криптографічні методи захисту інформації — ЇЄІҐ"


def encrypt_text(text: str, e: int, n: int) -> str:
    k = (n.bit_length() + 7) // 8
    chunk_size = k - 2
    data = text.encode("utf-8")
    out = bytearray()
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        m = int.from_bytes(b"\x01" + chunk, "big")
        c = rsa_encrypt(m, e, n)
        out += c.to_bytes(k, "big")
    return base64.b64encode(bytes(out)).decode("ascii")


def decrypt_text(ciphertext_b64: str, d: int, n: int) -> str:
    k = (n.bit_length() + 7) // 8
    raw = base64.b64decode(ciphertext_b64)
    out = bytearray()
    for i in range(0, len(raw), k):
        c = int.from_bytes(raw[i:i + k], "big")
        m = rsa_decrypt(c, d, n)
        block = m.to_bytes((m.bit_length() + 7) // 8, "big")
        out += block[1:]
    return out.decode("utf-8")


if __name__ == "__main__":
    keys = RSA(bits=512)
    e, n = keys.public_key
    d, _ = keys.private_key

    for text in (TEST_TEXT, UKR_TEXT):
        encrypted = encrypt_text(text, e, n)
        decrypted = decrypt_text(encrypted, d, n)
        print(f"Відкритий текст: {text}")
        print(f"Шифротекст (Base64): {encrypted}")
        print(f"Розшифрований текст: {decrypted}")
        print(f"Збіг: {decrypted == text}")
        print("-" * 40)
