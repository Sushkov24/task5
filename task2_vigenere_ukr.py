UKR_ALPHABET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
SURNAME = "СУШКОВ"
PLAINTEXT = "криптографічніметодизахистуінформації"


def normalize(text: str) -> str:
    return "".join(ch for ch in text.upper() if ch in UKR_ALPHABET)


def vigenere_encrypt(text: str, key: str) -> str:
    text = normalize(text)
    key = normalize(key)
    n = len(UKR_ALPHABET)
    result = []
    for i, ch in enumerate(text):
        shift = UKR_ALPHABET.index(key[i % len(key)])
        result.append(UKR_ALPHABET[(UKR_ALPHABET.index(ch) + shift) % n])
    return "".join(result)


def vigenere_decrypt(text: str, key: str) -> str:
    text = normalize(text)
    key = normalize(key)
    n = len(UKR_ALPHABET)
    result = []
    for i, ch in enumerate(text):
        shift = UKR_ALPHABET.index(key[i % len(key)])
        result.append(UKR_ALPHABET[(UKR_ALPHABET.index(ch) - shift) % n])
    return "".join(result)


if __name__ == "__main__":
    encrypted = vigenere_encrypt(PLAINTEXT, SURNAME)
    decrypted = vigenere_decrypt(encrypted, SURNAME)
    print(f"Відкритий текст: {normalize(PLAINTEXT)}")
    print(f"Ключ:            {normalize(SURNAME)}")
    print(f"Шифротекст:      {encrypted}")
    print(f"Розшифрований:   {decrypted}")
    print(f"Збіг: {normalize(PLAINTEXT) == decrypted}")
