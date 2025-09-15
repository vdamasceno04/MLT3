import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# --- Configurações da Criptografia AES em modo CBC---

# Chave principal, deve ser a mesma para quem envia e quem recebe.
KEY = b"minha-chave"

# Número de 'embaralhamentos' para deixar a chave mais forte.
ITERATIONS = 100000

# Tamanho da chave em bytes (16 = AES-128).
KEY_SIZE = 16 
# Tamanho do bloco do AES (sempre 16 bytes).
BLOCK_SIZE = 16

# --- Funções de Conversão ---

def to_bytes(texto: str) -> bytes:
    """Converte texto para bytes (usando latin-1 para caracteres especiais)."""
    return texto.encode('latin-1')

def bytes_to_text(data: bytes) -> str:
    """Converte bytes de volta para texto."""
    return data.decode('latin-1')

def to_binary_stream(data: bytes) -> str:
    """Converte bytes para uma string de 0s e 1s."""
    return "".join(f"{byte:08b}" for byte in data)

def binary_stream_to_bytes(bin_stream: str) -> bytes:
    """Converte a string de 0s e 1s de volta para bytes."""
    return bytes([int(bin_stream[i:i+8], 2) for i in range(0, len(bin_stream), 8)])


def encrypt(data_bytes: bytes) -> bytes:
    """Criptografa os dados usando AES."""

    # Gera um 'salt' aleatório. Impede que textos iguais tenham resultados iguais.
    salt = get_random_bytes(16)

    # Fortalece nossa chave principal usando o salt. Protege contra força bruta.
    derived_key = hashlib.pbkdf2_hmac('sha256', KEY, salt, ITERATIONS, dklen=KEY_SIZE)

    # Prepara a cifra AES no modo CBC, que liga um bloco ao outro.
    # Um IV (Vetor de Inicialização) aleatório é criado para dar início ao processo.
    cipher = AES.new(derived_key, AES.MODE_CBC)
    iv = cipher.iv

    # Garante que a mensagem tenha o tamanho certo para o AES (múltiplo de 16)
    # e depois criptografa de fato.
    ciphertext = cipher.encrypt(pad(data_bytes, BLOCK_SIZE))

    # Monta o pacote final para envio: salt + iv + dados criptografados.
    # O receptor vai precisar de tudo isso para reverter.
    return salt + iv + ciphertext


def decrypt(encrypted_data: bytes) -> bytes:
    """Descriptografa os dados recebidos."""

    # Separa o pacote recebido em suas três partes.
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]

    # Recria a chave exata que foi usada na criptografia, usando o salt recebido.
    derived_key = hashlib.pbkdf2_hmac('sha256', KEY, salt, ITERATIONS, dklen=KEY_SIZE)

    # Prepara a cifra para descriptografar, usando a chave e o IV corretos.
    cipher = AES.new(derived_key, AES.MODE_CBC, iv)

    # Descriptografa e remove os bytes extras do padding para restaurar a mensagem original.
    decrypted_bytes = unpad(cipher.decrypt(ciphertext), BLOCK_SIZE)

    return decrypted_bytes