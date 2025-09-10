def to_bytes(texto: str, encoding: str = 'latin-1', separador: str = ' ') -> bytes:
    return texto.encode(encoding)


def encrypt(word: bytes) -> bytes:
    return word

def to_binary_stream(data: bytes) -> str:
    return "".join(f"{byte:08b}" for byte in data)