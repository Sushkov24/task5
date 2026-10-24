ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CIPHERTEXT = "vppanlwxlyopyncjae"


def caesar_decrypt(text: str, key: int) -> str:
    result = []
    for ch in text:
        if ch in ALPHABET:
            result.append(ALPHABET[(ALPHABET.index(ch) - key) % len(ALPHABET)])
        else:
            result.append(ch)
    return "".join(result)


def brute_force(ciphertext: str) -> None:
    print(f"Шифротекст: {ciphertext}")
    print("-" * 40)
    for key in range(len(ALPHABET)):
        print(f"ключ = {key:2d}: {caesar_decrypt(ciphertext, key)}")


if __name__ == "__main__":
    brute_force(CIPHERTEXT)
