def tobinary(texto: str, encoding: str = 'latin-1', separador: str = ' ') -> bytes:
    return texto.encode(encoding)


def encrypt(word: bytes) -> bytes:
    return word
