import socket
import json

PORTA = 65432  # Porta padrão

def enviar_sinal(ip_destino, lista_sinal_mlt3):
    """
    Conecta no outro PC e envia a lista do sinal MLT-3.
    """
    try:
        # 1. Serializa a lista para JSON (transforma em texto)
        dados_json = json.dumps(lista_sinal_mlt3)
        dados_bytes = dados_json.encode('utf-8')

        # 2. Cria o socket e conecta
        print(f"Tentando conectar em {ip_destino}:{PORTA}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_destino, PORTA))
            s.sendall(dados_bytes)
            print("Dados enviados com sucesso!")
            
    except ConnectionRefusedError:
        print("ERRO: Não foi possível conectar. O Host B está ouvindo?")
    except Exception as e:
        print(f"ERRO de Rede: {e}")

def receber_sinal():
    """
    Fica ouvindo na porta e espera receber os dados.
    Retorna a lista do sinal MLT-3 quando chegar.
    """
    print(f"Aguardando conexão na porta {PORTA}...")
    print(f"Descubra seu IP com o comando 'ip a' e informe ao Host A.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', PORTA))
        s.listen()
        conn, addr = s.accept()
        
        with conn:
            print(f"Conectado por {addr}")
            buffer_dados = b""
            
            # Recebe os dados em pedaços (chunks)
            while True:
                pedaco = conn.recv(4096)
                if not pedaco:
                    break
                buffer_dados += pedaco
            
            # Decodifica o JSON de volta para Lista Python
            lista_recebida = json.loads(buffer_dados.decode('utf-8'))
            return lista_recebida