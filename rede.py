import socket
import json

# Porta aleatória alta pra não dar conflito no PC
PORTA_DO_ROLE = 65432

def enviar_sinal(ip_do_camarada, lista_do_sinal):
    # Tenta conectar no outro PC e jogar a lista lá
    try:
        # Transforma a lista do Python num textão (JSON) e depois em bytes
        # pq o socket é chato e só aceita byte
        pacote_texto = json.dumps(lista_do_sinal)
        pacote_bytes = pacote_texto.encode('utf-8')

        print(f"Batendo na porta do IP {ip_do_camarada}...")
        
        # Cria o 'telefone' (socket) e disca pro amigo
        # AF_INET = IPv4, SOCK_STREAM = TCP (garante que chega)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as canal:
            canal.connect((ip_do_camarada, PORTA_DO_ROLE))
            canal.sendall(pacote_bytes)
            print("Enviado com sucesso!")
            
    except ConnectionRefusedError:
        print("VISH: Ninguém atendeu. O Host B tá rodando o código?")
    except Exception as e:
        print(f"Deu ruim na rede: {e}")

def receber_sinal():
    # Fica plantado esperando chegar conexão
    print(f"Ouvindo tudo na porta {PORTA_DO_ROLE}...")
    print(f"Vê teu IP aí (ip a / ipconfig) e passa pro Host A.")

    # 0.0.0.0 aceita conexão de qualquer placa de rede do PC
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind(('0.0.0.0', PORTA_DO_ROLE))
        servidor.listen()
        
        # O código trava nessa linha até alguém conectar
        conexao, endereco_do_remetente = servidor.accept()
        
        with conexao:
            print(f"Opa, conectou gente do IP: {endereco_do_remetente}")
            tudo_que_chegou = b""
            
            # Loop pra pegar os dados em pedacinhos de 4kb
            while True:
                pedacinho = conexao.recv(4096)
                if not pedacinho:
                    # Se veio vazio, acabou a transmissão
                    break
                tudo_que_chegou += pedacinho
            
            # Transforma a bagunça de bytes de volta pra Lista Python
            lista_final = json.loads(tudo_que_chegou.decode('utf-8'))
            return lista_final