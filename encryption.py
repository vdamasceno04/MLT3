import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Configurações
MINHA_SENHA = b"minha-chave"
RODADAS = 100000
TAMANHO_CHAVE = 16 
TAMANHO_BLOCO = 16

def texto_pra_bytes(texto: str) -> bytes:
    return texto.encode('latin-1')

def bytes_pra_texto(dados: bytes) -> str:
    return dados.decode('latin-1')

def bytes_pra_binario_string(dados: bytes) -> str:
    return "".join(f"{byte:08b}" for byte in dados)

def binario_string_pra_bytes(tripa_binaria: str) -> bytes:
    lista_inteiros = [int(tripa_binaria[i:i+8], 2) for i in range(0, len(tripa_binaria), 8)]
    return bytes(lista_inteiros)


def criptografar_tudo(dados_em_bytes: bytes) -> bytes:
    salzinho = get_random_bytes(16)
    
    # Deriva a chave usando PBKDF2
    chave_tunada = hashlib.pbkdf2_hmac('sha256', MINHA_SENHA, salzinho, RODADAS, dklen=TAMANHO_CHAVE)

    cifrador = AES.new(chave_tunada, AES.MODE_CBC)
    vetor_inicial = cifrador.iv

    texto_baguncado = cifrador.encrypt(pad(dados_em_bytes, TAMANHO_BLOCO))

    # Retorna tudo junto: Salt + IV + Conteúdo
    return salzinho + vetor_inicial + texto_baguncado


def descriptografar_tudo(pacote_recebido: bytes) -> bytes:
    # Separa os componentes
    salzinho = pacote_recebido[:16]
    vetor_inicial = pacote_recebido[16:32]
    conteudo_trancado = pacote_recebido[32:]

    chave_tunada = hashlib.pbkdf2_hmac('sha256', MINHA_SENHA, salzinho, RODADAS, dklen=TAMANHO_CHAVE)

    cifrador = AES.new(chave_tunada, AES.MODE_CBC, vetor_inicial)
    
    bytes_limpos = unpad(cifrador.decrypt(conteudo_trancado), TAMANHO_BLOCO)

    return bytes_limpos